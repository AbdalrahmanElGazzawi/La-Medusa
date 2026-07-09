/* La Medusa — inquiry form (EN + AR pages share this file).
   Anonymous insert into `inquiries`; RLS allows write-only for the public. */
(function () {
  "use strict";
  var lang = document.documentElement.lang === "ar" ? "ar" : "en";
  var T = lang === "ar" ? {
    sent: "وصلتنا رسالتك — سنرد عليك خلال يومي عمل. شكراً!",
    short: "اكتبي رسالة من ٥ أحرف على الأقل.",
    fail: "تعذّر الإرسال — حاولي مرة أخرى أو راسلينا على واتساب."
  } : {
    sent: "Got it — we'll get back to you within two working days. Thank you!",
    short: "Please write a message of at least 5 characters.",
    fail: "Couldn't send — try again, or message us on WhatsApp."
  };

  function $(id) { return document.getElementById(id); }
  function waitDb(cb) { if (window.LM_DB) return cb(window.LM_DB); setTimeout(function () { waitDb(cb); }, 150); }

  /* preselect topic from ?topic= */
  var params = new URLSearchParams(location.search);
  var topic = params.get("topic");
  var sel = $("inq-topic");
  if (topic && sel && ["retreat", "corporate", "hammocks", "general"].indexOf(topic) !== -1) sel.value = topic;

  waitDb(function (db) {
    $("form-inquire").addEventListener("submit", function (e) {
      e.preventDefault();
      var m = $("inq-msg-status");
      var message = $("inq-message").value.trim();
      if (message.length < 5) { m.textContent = T.short; m.className = "auth-msg err"; return; }
      var btn = $("inq-submit"); btn.disabled = true;
      db.from("inquiries").insert({
        topic: sel.value,
        name: $("inq-name").value.trim(),
        contact: $("inq-contact").value.trim(),
        message: message,
        lang: lang
      }).then(function (r) {
        btn.disabled = false;
        if (r.error) { m.textContent = T.fail; m.className = "auth-msg err"; return; }
        m.textContent = T.sent; m.className = "auth-msg ok";
        $("form-inquire").reset();
      });
    });
  });
})();
