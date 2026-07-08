/* La Medusa — behavior layer (no dependencies) */
(function () {
  "use strict";
  var cfg = window.LM_CONFIG || {};
  var lang = document.documentElement.lang === "ar" ? "ar" : "en";

  /* ----- WhatsApp deep links -----
     Any element with [data-wa="context"] becomes a wa.me link with a prefilled message.
     Phase 2: when cfg.bookingEnabled is true, elements with [data-book] route to /book/ instead. */
  function waUrl(context) {
    var msgs = (cfg.waMessages && cfg.waMessages[lang]) || {};
    var msg = msgs[context] || msgs.general || "";
    return "https://wa.me/" + cfg.whatsappNumber + "?text=" + encodeURIComponent(msg);
  }
  document.querySelectorAll("[data-wa]").forEach(function (el) {
    if (cfg.bookingEnabled && el.hasAttribute("data-book")) {
      el.setAttribute("href", (lang === "ar" ? "/ar" : "") + "/book/");
      return;
    }
    el.setAttribute("href", waUrl(el.getAttribute("data-wa")));
    el.setAttribute("target", "_blank");
    el.setAttribute("rel", "noopener");
  });

  /* ----- mobile nav ----- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      document.body.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ----- reveal on scroll ----- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });
  }

  /* ----- analytics (loads only when IDs are set in config.js) ----- */
  if (cfg.ga4Id) {
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + cfg.ga4Id;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", cfg.ga4Id);
  }
  if (cfg.metaPixelId) {
    !(function (f, b, e, v, n, t) {
      if (f.fbq) return; n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = true; n.version = "2.0"; n.queue = [];
      t = b.createElement(e); t.async = true; t.src = v;
      b.getElementsByTagName(e)[0].parentNode.insertBefore(t, b.getElementsByTagName(e)[0]);
    })(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
    window.fbq("init", cfg.metaPixelId);
    window.fbq("track", "PageView");
  }

  /* ----- outbound WhatsApp click tracking (fires when analytics live) ----- */
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("[data-wa]");
    if (!a) return;
    var ctx = a.getAttribute("data-wa");
    if (window.gtag) window.gtag("event", "whatsapp_click", { cta_context: ctx, page_lang: lang });
    if (window.fbq) window.fbq("trackCustom", "WhatsAppClick", { context: ctx, lang: lang });
  });
})();
