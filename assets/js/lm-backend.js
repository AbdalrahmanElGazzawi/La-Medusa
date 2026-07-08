/* La Medusa — live data layer (Supabase). Loads only when config has credentials.
   Public pages: live schedule, admin-managed photos, public announcements.
   Pages degrade gracefully to their static content if this never runs. */
(function () {
  "use strict";
  var cfg = window.LM_CONFIG || {};
  if (!cfg.supabaseUrl || !cfg.supabaseAnonKey) return;
  var lang = document.documentElement.lang === "ar" ? "ar" : "en";

  var s = document.createElement("script");
  s.src = "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js";
  s.onload = init;
  document.head.appendChild(s);

  var DAYS = {
    en: ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    ar: ["", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
  };

  function esc(t) { var d = document.createElement("div"); d.textContent = t == null ? "" : t; return d.innerHTML; }

  function init() {
    var db = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey);
    window.LM_DB = db;

    /* ---- live schedule table ---- */
    var tb = document.querySelector("[data-live-schedule]");
    if (tb) {
      db.from("schedule_slots").select("*").eq("active", true)
        .order("day_of_week").order("sort")
        .then(function (r) {
          if (r.error || !r.data || !r.data.length) return;
          var byDay = {};
          r.data.forEach(function (x) { (byDay[x.day_of_week] = byDay[x.day_of_week] || []).push(x); });
          var html = "";
          Object.keys(byDay).sort().forEach(function (d) {
            var cells = byDay[d].map(function (x) {
              var name = lang === "ar" ? x.class_ar : x.class_en;
              var lvl = lang === "ar" ? x.level_ar : x.level_en;
              var price = x.price_egp ? " · " + x.price_egp + (lang === "ar" ? " ج.م" : " EGP") : "";
              return '<span class="cls">' + esc(name) + "</span><br><span class=\"meta\">" + esc(x.time_label) + (lvl ? " · " + esc(lvl) : "") + esc(price) + "</span>";
            }).join("<br><br>");
            html += '<tr><th scope="row" class="cls">' + DAYS[lang][d] + "</th><td>" + cells + "</td></tr>";
          });
          var head = tb.closest("table").querySelector("thead tr");
          if (head) head.innerHTML = '<th scope="col">' + (lang === "ar" ? "اليوم" : "Day") + '</th><th scope="col">' + (lang === "ar" ? "الحصص" : "Classes") + "</th>";
          tb.innerHTML = html;
          var badge = document.querySelector("[data-schedule-status]");
          if (badge) badge.textContent = lang === "ar" ? "جدول محدّث مباشرةً من الاستوديو" : "Live schedule — updated by the studio";
        });
    }

    /* ---- admin-managed photos ---- */
    var slots = document.querySelectorAll("[data-photo-slot]");
    if (slots.length) {
      db.from("gallery").select("*").then(function (r) {
        if (r.error || !r.data) return;
        var map = {};
        r.data.forEach(function (g) { map[g.slot_key] = g; });
        slots.forEach(function (el) {
          var g = map[el.getAttribute("data-photo-slot")];
          if (!g || !g.image_url) return;
          var img = document.createElement("img");
          img.src = g.image_url;
          img.alt = (lang === "ar" ? g.alt_ar : g.alt_en) || "";
          img.loading = "lazy";
          img.className = "live";
          el.classList.add("has-live");
          el.appendChild(img);
        });
      });
    }

    /* ---- public announcements strip ---- */
    var news = document.querySelector("[data-live-news]");
    if (news) {
      db.from("events").select("*").eq("published", true).eq("members_only", false)
        .order("created_at", { ascending: false }).limit(1)
        .then(function (r) {
          if (r.error || !r.data || !r.data.length) return;
          var e = r.data[0];
          var title = lang === "ar" ? (e.title_ar || e.title_en) : e.title_en;
          var body = lang === "ar" ? (e.body_ar || e.body_en) : e.body_en;
          news.innerHTML = '<div class="news-strip"><strong>' + esc(title) + "</strong> — " + esc(body) + "</div>";
        });
    }
  }
})();
