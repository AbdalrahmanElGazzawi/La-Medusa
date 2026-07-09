/* La Medusa — studio management panel (admins only; RLS enforces server-side) */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  function esc(t) { var d = document.createElement("div"); d.textContent = t == null ? "" : t; return d.innerHTML; }
  function attr(t) { return esc(t).replace(/"/g, "&quot;"); }
  function waitDb(cb) { if (window.LM_DB) return cb(window.LM_DB); setTimeout(function () { waitDb(cb); }, 150); }

  var DAYS = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
  var SLOT_DEFS = [
    ["home_studio", "Home — studio / cocoon ending"],
    ["retreat_home", "Home — retreat teaser"],
    ["ayttc_2025", "Teacher training — April 2025 cohort"],
    ["ayttc_2026", "Teacher training — April 2026 cohort"],
    ["retreat_2025", "Retreats — 2025 group photo"],
    ["teacher_mona", "Teachers — Mona portrait"],
    ["teacher_reem", "Teachers — Reem portrait"],
    ["hammocks_fabric", "Hammocks — fabric colors"],
    ["hammocks_atelier", "Hammocks — the atelier"]
  ];

  waitDb(function (db) {
    db.auth.getSession().then(function (r) {
      var session = r.data && r.data.session;
      if (!session) { $("gate").innerHTML = 'Please <a href="/account/">sign in</a> first, then return to this page.'; return; }
      db.from("profiles").select("role").eq("id", session.user.id).single().then(function (p) {
        if (!p.data || p.data.role !== "admin") {
          $("gate").textContent = "This area is for studio admins. Ask an existing admin to add your email in the Admins tab.";
          return;
        }
        $("gate").style.display = "none";
        $("panel-wrap").style.display = "";
        boot(db);
      });
    });
  });

  function boot(db) {
    document.querySelectorAll(".admin-tabs button").forEach(function (b) {
      b.addEventListener("click", function () {
        document.querySelectorAll(".admin-tabs button").forEach(function (x) { x.classList.remove("on"); });
        document.querySelectorAll(".admin-panel").forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
        $("panel-" + b.dataset.p).classList.add("on");
      });
    });

    /* ----- schedule ----- */
    function loadSchedule() {
      db.from("schedule_slots").select("*").order("day_of_week").order("sort").then(function (r) {
        if (r.error) return alert(r.error.message);
        $("sched-body").innerHTML = r.data.map(function (x) {
          var dayOpts = DAYS.map(function (d, i) { return i ? '<option value="' + i + '"' + (i === x.day_of_week ? " selected" : "") + ">" + d + "</option>" : ""; }).join("");
          return '<tr data-id="' + x.id + '">' +
            '<td><select data-f="day_of_week">' + dayOpts + "</select></td>" +
            '<td><input data-f="time_label" value="' + attr(x.time_label) + '"></td>' +
            '<td><input data-f="class_en" value="' + attr(x.class_en) + '"></td>' +
            '<td><input data-f="class_ar" dir="rtl" value="' + attr(x.class_ar) + '"></td>' +
            '<td><input data-f="level_en" value="' + attr(x.level_en) + '"></td>' +
            '<td><input data-f="price_egp" type="number" value="' + (x.price_egp || "") + '" placeholder="—"></td>' +
            '<td><input data-f="capacity" type="number" min="1" max="40" value="' + (x.capacity || 8) + '" style="width:56px"></td>' +
            '<td><input data-f="active" type="checkbox"' + (x.active ? " checked" : "") + "></td>" +
            '<td style="white-space:nowrap"><button class="btn btn-sea btn-sm" data-act="save">Save</button> ' +
            '<button class="btn btn-danger btn-sm" data-act="del">Delete</button></td></tr>';
        }).join("");
      });
    }
    $("sched-body").addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-act]"); if (!btn) return;
      var tr = btn.closest("tr"), id = tr.dataset.id;
      if (btn.dataset.act === "del") {
        if (!confirm("Delete this class slot?")) return;
        db.from("schedule_slots").delete().eq("id", id).then(function (r) { r.error ? alert(r.error.message) : loadSchedule(); });
        return;
      }
      var upd = {};
      tr.querySelectorAll("[data-f]").forEach(function (inp) {
        var f = inp.dataset.f;
        if (f === "active") upd[f] = inp.checked;
        else if (f === "day_of_week") upd[f] = parseInt(inp.value, 10);
        else if (f === "price_egp") upd[f] = inp.value ? parseInt(inp.value, 10) : null;
        else if (f === "capacity") upd[f] = Math.min(40, Math.max(1, parseInt(inp.value, 10) || 8));
        else upd[f] = inp.value;
      });
      db.from("schedule_slots").update(upd).eq("id", id).then(function (r) { r.error ? alert(r.error.message) : loadSchedule(); });
    });
    $("btn-add-slot").addEventListener("click", function () {
      db.from("schedule_slots").insert({ day_of_week: 1, period: "sunset", time_label: "7:00 PM", class_en: "New class", class_ar: "حصة جديدة", sort: 99 })
        .then(function (r) { r.error ? alert(r.error.message) : loadSchedule(); });
    });

    /* ----- events ----- */
    function loadEvents() {
      db.from("events").select("*").order("created_at", { ascending: false }).then(function (r) {
        if (r.error) return alert(r.error.message);
        $("ev-body").innerHTML = r.data.map(function (x) {
          return '<tr data-id="' + x.id + '">' +
            '<td><select data-f="kind"><option' + (x.kind === "event" ? " selected" : "") + '>event</option><option' + (x.kind === "announcement" ? " selected" : "") + ">announcement</option></select></td>" +
            '<td><input data-f="title_en" value="' + attr(x.title_en) + '"><input data-f="title_ar" dir="rtl" style="margin-top:4px" value="' + attr(x.title_ar) + '"></td>' +
            '<td><input data-f="body_en" value="' + attr(x.body_en) + '"><input data-f="body_ar" dir="rtl" style="margin-top:4px" value="' + attr(x.body_ar) + '"></td>' +
            '<td><input data-f="starts_on" type="date" value="' + (x.starts_on || "") + '"></td>' +
            '<td><input data-f="published" type="checkbox"' + (x.published ? " checked" : "") + "></td>" +
            '<td><input data-f="members_only" type="checkbox"' + (x.members_only ? " checked" : "") + "></td>" +
            '<td style="white-space:nowrap"><button class="btn btn-sea btn-sm" data-act="save">Save</button> ' +
            '<button class="btn btn-danger btn-sm" data-act="del">Delete</button></td></tr>';
        }).join("");
      });
    }
    $("ev-body").addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-act]"); if (!btn) return;
      var tr = btn.closest("tr"), id = tr.dataset.id;
      if (btn.dataset.act === "del") {
        if (!confirm("Delete this item?")) return;
        db.from("events").delete().eq("id", id).then(function (r) { r.error ? alert(r.error.message) : loadEvents(); });
        return;
      }
      var upd = {};
      tr.querySelectorAll("[data-f]").forEach(function (inp) {
        var f = inp.dataset.f;
        if (inp.type === "checkbox") upd[f] = inp.checked;
        else if (f === "starts_on") upd[f] = inp.value || null;
        else upd[f] = inp.value;
      });
      db.from("events").update(upd).eq("id", id).then(function (r) { r.error ? alert(r.error.message) : loadEvents(); });
    });
    $("btn-add-event").addEventListener("click", function () {
      db.from("events").insert({ kind: "event", title_en: "New event", published: false })
        .then(function (r) { r.error ? alert(r.error.message) : loadEvents(); });
    });

    /* ----- photos ----- */
    function loadPhotos() {
      db.from("gallery").select("*").then(function (r) {
        var map = {};
        (r.data || []).forEach(function (g) { map[g.slot_key] = g; });
        $("photo-list").innerHTML = SLOT_DEFS.map(function (s) {
          var g = map[s[0]];
          var thumb = g ? '<img class="thumb" src="' + attr(g.image_url) + '" alt="">' : '<div class="thumb"></div>';
          return '<div class="slot-card" data-slot="' + s[0] + '">' + thumb +
            '<div class="grow"><strong>' + s[1] + "</strong><span>" + s[0] + (g ? "" : " · no photo yet — placeholder art is shown on the site") + "</span>" +
            '<input type="text" data-f="alt" placeholder="Describe the photo (alt text)" value="' + (g ? attr(g.alt_en) : "") + '" style="margin-top:6px;width:100%;padding:7px 9px;border:1px solid var(--sea-tint-2);border-radius:8px;font-size:13px"></div>' +
            '<label class="btn btn-ghost btn-sm" style="cursor:pointer">Upload<input type="file" accept="image/*" hidden></label></div>';
        }).join("");
      });
    }
    $("photo-list").addEventListener("change", function (e) {
      var inp = e.target;
      if (inp.type !== "file" || !inp.files.length) return;
      var card = inp.closest(".slot-card"), key = card.dataset.slot;
      var file = inp.files[0];
      if (file.size > 4 * 1024 * 1024) return alert("Please choose an image under 4 MB (resize/compress first — smaller photos keep the site fast in Dahab).");
      var path = "slots/" + key + "-" + Date.now() + "." + (file.name.split(".").pop() || "jpg");
      card.style.opacity = 0.5;
      window.LM_DB.storage.from("site-photos").upload(path, file, { upsert: true }).then(function (r) {
        if (r.error) { card.style.opacity = 1; return alert(r.error.message); }
        var url = window.LM_DB.storage.from("site-photos").getPublicUrl(path).data.publicUrl;
        var alt = card.querySelector('[data-f="alt"]').value;
        window.LM_DB.from("gallery").upsert({ slot_key: key, image_url: url, alt_en: alt, alt_ar: alt, updated_at: new Date().toISOString() })
          .then(function (r2) { card.style.opacity = 1; r2.error ? alert(r2.error.message) : loadPhotos(); });
      });
    });

    /* ----- bookings ----- */
    function loadBookings() {
      var today = new Date().toISOString().slice(0, 10);
      db.from("bookings")
        .select("*, schedule_slots(class_en, time_label, capacity), profiles(full_name, email)")
        .eq("status", "confirmed").gte("class_date", today)
        .order("class_date").order("created_at")
        .then(function (r) {
          if (r.error) return alert(r.error.message);
          if (!r.data.length) { $("bookings-body").innerHTML = '<tr><td colspan="5">No upcoming bookings yet.</td></tr>'; return; }
          var counts = {};
          r.data.forEach(function (b) { var k = b.slot_id + "|" + b.class_date; counts[k] = (counts[k] || 0) + 1; });
          $("bookings-body").innerHTML = r.data.map(function (b) {
            var s = b.schedule_slots || {}, p = b.profiles || {};
            var k = b.slot_id + "|" + b.class_date;
            return '<tr data-id="' + b.id + '">' +
              "<td>" + esc(b.class_date) + "</td>" +
              "<td>" + esc(s.class_en) + " · " + esc(s.time_label) + "</td>" +
              "<td>" + esc(p.full_name || "—") + "</td>" +
              