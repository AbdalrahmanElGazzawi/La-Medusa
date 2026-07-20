/* La Medusa — booking page logic (EN + AR pages share this file).
   Requires a signed-in member. Capacity is enforced server-side (book_slot RPC). */
(function () {
  "use strict";
  var cfg = window.LM_CONFIG || {};
  var lang = document.documentElement.lang === "ar" ? "ar" : "en";
  var DAYS_AHEAD = 14;

  var T = lang === "ar" ? {
    signIn: 'الحجز للأعضاء — <a href="/ar/account/">سجّلي الدخول أو أنشئي حساباً مجانياً</a> ثم عودي إلى هذه الصفحة.',
    seatsLeft: function (n) { return n === 1 ? "مقعد واحد متبقٍ" : n + " مقاعد متبقية"; },
    full: "مكتملة",
    book: "احجزي",
    booked: "محجوزة ✓",
    cancel: "إلغاء",
    myBookings: "حجوزاتك القادمة",
    noBookings: "لا توجد حجوزات قادمة بعد — اختاري حصة من القائمة.",
    confirmCancel: "إلغاء هذا الحجز؟",
    successTitle: "تم الحجز!",
    successBody: "مقعدك محفوظ. أرسلي رسالة التأكيد عبر واتساب حتى يعرف الاستوديو أنك قادمة:",
    waConfirm: "تأكيد عبر واتساب",
    egp: " ج.م",
    loading: "جارٍ تحميل الجدول…",
    morning: "صباحية",
    sunset: "غروب",
    all: "كل الحصص",
    noClasses: "لا توجد حصص متاحة للحجز حالياً — راسلينا على واتساب وسنساعدك.",
    errors: {
      SIGN_IN_REQUIRED: "سجّلي الدخول أولاً.",
      SLOT_UNAVAILABLE: "هذه الحصة لم تعد متاحة.",
      DATE_PASSED: "هذا التاريخ قد مضى.",
      TOO_FAR_AHEAD: "الحجز متاح حتى ٣٠ يوماً مقدماً.",
      DATE_DAY_MISMATCH: "التاريخ لا يطابق يوم الحصة.",
      CLASS_FULL: "الحصة مكتملة — راسلينا على واتساب لقائمة الانتظار.",
      ALREADY_BOOKED: "لديك حجز في هذه الحصة بالفعل.",
      NOT_CANCELLABLE: "تعذّر إلغاء هذا الحجز."
    },
    waMsg: function (cls, date, time) {
      return "BOOKING — مرحباً! حجزت \"" + cls + "\" يوم " + date + " الساعة " + time + " عبر الموقع — أؤكد حضوري.";
    }
  } : {
    signIn: 'Booking is for members — <a href="/account/">sign in or create a free account</a>, then come back to this page.',
    seatsLeft: function (n) { return n === 1 ? "1 seat left" : n + " seats left"; },
    full: "Full",
    book: "Book",
    booked: "Booked ✓",
    cancel: "Cancel",
    myBookings: "Your upcoming bookings",
    noBookings: "No upcoming bookings yet — pick a class from the list.",
    confirmCancel: "Cancel this booking?",
    successTitle: "You're booked!",
    successBody: "Your seat is held. Send the WhatsApp confirmation so the studio knows you're coming:",
    waConfirm: "Confirm on WhatsApp",
    egp: " EGP",
    loading: "Loading the schedule…",
    morning: "Morning",
    sunset: "Sunset",
    all: "All classes",
    noClasses: "No classes are open for booking right now — message us on WhatsApp and we\u2019ll help.",
    errors: {
      SIGN_IN_REQUIRED: "Please sign in first.",
      SLOT_UNAVAILABLE: "This class is no longer available.",
      DATE_PASSED: "That date has passed.",
      TOO_FAR_AHEAD: "Bookings open up to 30 days ahead.",
      DATE_DAY_MISMATCH: "That date doesn't match the class day.",
      CLASS_FULL: "This class is full — message us on WhatsApp for the waitlist.",
      ALREADY_BOOKED: "You already have a booking for this class.",
      NOT_CANCELLABLE: "This booking can't be cancelled."
    },
    waMsg: function (cls, date, time) {
      return "BOOKING — Hi! I booked \"" + cls + "\" on " + date + " at " + time + " via the website — confirming my spot.";
    }
  };

  function $(id) { return document.getElementById(id); }
  function esc(t) { var d = document.createElement("div"); d.textContent = t == null ? "" : t; return d.innerHTML; }
  function waitDb(cb) { if (window.LM_DB) return cb(window.LM_DB); setTimeout(function () { waitDb(cb); }, 150); }
  function friendly(err) {
    var m = (err && err.message) || "";
    for (var k in T.errors) if (m.indexOf(k) !== -1) return T.errors[k];
    return m || "Error";
  }
  function iso(d) {
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }
  function isodow(d) { return (d.getDay() + 6) % 7 + 1; } /* 1=Mon … 7=Sun */
  function fmtDate(d) {
    return d.toLocaleDateString(lang === "ar" ? "ar-EG" : "en-GB", { weekday: "long", day: "numeric", month: "long" });
  }

  waitDb(function (db) {
    db.auth.getSession().then(function (r) {
      var session = r.data && r.data.session;
      if (!session) { $("book-gate").innerHTML = T.signIn; return; }
      $("book-gate").style.display = "none";
      $("book-view").style.display = "";
      boot(db, session);
    });
  });

  function boot(db, session) {
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var end = new Date(today); end.setDate(end.getDate() + DAYS_AHEAD - 1);
    var myName = ((session.user.user_metadata && session.user.user_metadata.full_name) || "").split(" ")[0];
    var filterCls = "";
    var S = { slots: [], avail: {}, mineKeys: {} };

    function load() {
      $("book-days").innerHTML = "<p class='sec-lead'>" + T.loading + "</p>";
      Promise.all([
        db.from("schedule_slots").select("*").eq("active", true).order("sort"),
        db.rpc("slot_availability", { p_from: iso(today), p_to: iso(end) }),
        db.from("bookings").select("*, schedule_slots(class_en, class_ar, time_label)")
          .eq("user_id", session.user.id).eq("status", "confirmed").gte("class_date", iso(today))
          .order("class_date")
      ]).then(function (res) {
        S.slots = res[0].data || [];
        S.avail = {};
        (res[1].data || []).forEach(function (a) { S.avail[a.slot_id + "|" + a.class_date] = a.booked; });
        var mine = res[2].data || [];
        S.mineKeys = {};
        mine.forEach(function (b) { S.mineKeys[b.slot_id + "|" + b.class_date] = b.id; });
        buildFilters();
        renderDays(S.slots, S.avail, S.mineKeys);
        renderMine(mine);
      });
    }

    function buildFilters() {
      var box = $("book-filters");
      if (!box) return;
      var names = {};
      S.slots.forEach(function (s) { names[lang === "ar" ? s.class_ar : s.class_en] = s.class_en; });
      var keys = Object.keys(names).sort();
      if (keys.length < 2) { box.hidden = true; return; }
      box.hidden = false;
      box.innerHTML = '<button data-fc=""' + (filterCls ? "" : ' class="on"') + ">" + T.all + "</button>" +
        keys.map(function (n) {
          return '<button data-fc="' + esc(names[n]) + '"' + (filterCls === names[n] ? ' class="on"' : "") + ">" + esc(n) + "</button>";
        }).join("");
    }
    document.addEventListener("click", function (e) {
      var fb = e.target.closest("[data-fc]");
      if (!fb) return;
      filterCls = fb.getAttribute("data-fc");
      buildFilters();
      renderDays(S.slots, S.avail, S.mineKeys);
    });

    function renderDays(slots, avail, mineKeys) {
      var html = "";
      for (var i = 0; i < DAYS_AHEAD; i++) {
        var d = new Date(today); d.setDate(d.getDate() + i);
        var dow = isodow(d), dateStr = iso(d);
        var daySlots = slots.filter(function (s) { return s.day_of_week === dow && (!filterCls || s.class_en === filterCls); });
        if (!daySlots.length) continue;
        var rows = daySlots.map(function (s) {
          var key = s.id + "|" + dateStr;
          var booked = avail[key] || 0;
          var left = Math.max(0, (s.capacity || 8) - booked);
          var name = lang === "ar" ? s.class_ar : s.class_en;
          var lvl = lang === "ar" ? s.level_ar : s.level_en;
          var price = s.price_egp ? " · " + s.price_egp + T.egp : "";
          var period = s.period === "morning" ? T.morning : T.sunset;
          var seat = left ? '<span class="seats">' + T.seatsLeft(left) + "</span>" : '<span class="seats seats-full">' + T.full + "</span>";
          var btn;
          if (mineKeys[key]) btn = '<span class="chip chip-lav">' + T.booked + "</span>";
          else if (!left) btn = '<button class="btn btn-ghost btn-sm" disabled>' + T.full + "</button>";
          else btn = '<button class="btn btn-primary btn-sm" data-book-slot="' + s.id + '" data-book-date="' + dateStr + '" data-cls="' + esc(name) + '" data-time="' + esc(s.time_label) + '">' + T.book + "</button>";
          return '<div class="book-row"><div class="grow"><strong>' + esc(name) + "</strong><br><span class=\"meta\">" + esc(s.time_label) + " · " + period + (lvl ? " · " + esc(lvl) : "") + esc(price) + " · " + seat + "</span></div>" + btn + "</div>";
        }).join("");
        html += '<div class="book-day reveal in"><h3>' + fmtDate(d) + "</h3>" + rows + "</div>";
      }
      $("book-days").innerHTML = html || "<p class='sec-lead'>" + T.noClasses + "</p>";
    }

    function renderMine(mine) {
      var box = $("my-bookings");
      if (!mine.length) { box.innerHTML = "<p class='sec-lead'>" + T.noBookings + "</p>"; return; }
      box.innerHTML = mine.map(function (b) {
        var s = b.schedule_slots || {};
        var name = lang === "ar" ? s.class_ar : s.class_en;
        var d = new Date(b.class_date + "T00:00:00");
        return '<div class="book-row"><div class="grow"><strong>' + esc(name) + "</strong><br><span class=\"meta\">" + fmtDate(d) + " · " + esc(s.time_label) + '</span></div><button class="btn btn-danger btn-sm" data-cancel="' + b.id + '">' + T.cancel + "</button></div>";
      }).join("");
    }

    document.addEventListener("click", function (e) {
      var b = e.target.closest("[data-book-slot]");
      if (b) {
        b.disabled = true;
        db.rpc("book_slot", { p_slot_id: b.getAttribute("data-book-slot"), p_class_date: b.getAttribute("data-book-date") })
          .then(function (r) {
            if (r.error) { b.disabled = false; return alert(friendly(r.error)); }
            var d = new Date(b.getAttribute("data-book-date") + "T00:00:00");
            var msg = T.waMsg(b.getAttribute("data-cls"), fmtDate(d), b.getAttribute("data-time"));
            if (myName) msg += " (" + myName + ")";
            var wa = "https://wa.me/" + cfg.whatsappNumber + "?text=" + encodeURIComponent(msg);
            $("book-success").innerHTML = '<div class="news-strip"><strong>' + T.successTitle + "</strong> — " + T.successBody +
              ' <a class="btn btn-primary btn-sm" target="_blank" rel="noopener" href="' + wa + '">' + T.waConfirm + "</a></div>";
            $("book-success").scrollIntoView({ behavior: "smooth", block: "center" });
            load();
          });
        return;
      }
      var c = e.target.closest("[data-cancel]");
      if (c) {
        if (!confirm(T.confirmCancel)) return;
        db.rpc("cancel_booking", { p_booking_id: c.getAttribute("data-cancel") })
          .then(function (r) { r.error ? alert(friendly(r.error)) : load(); });
      }
    });

    load();
  }
})();
