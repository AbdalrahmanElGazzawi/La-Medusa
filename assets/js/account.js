/* La Medusa — member account page logic (EN + AR pages share this file) */
(function () {
  "use strict";
  var cfg = window.LM_CONFIG || {};
  var lang = document.documentElement.lang === "ar" ? "ar" : "en";
  var T = lang === "ar" ? {
    badEmail: "أدخلي بريداً إلكترونياً صحيحاً.", shortPw: "كلمة المرور ٦ أحرف على الأقل.",
    checkInbox: "تحققي من بريدك الإلكتروني لتأكيد الحساب ثم عودي لتسجيل الدخول.",
    resetSent: "أرسلنا رابط إعادة تعيين كلمة المرور إلى بريدك.",
    welcome: "أهلاً", signedOut: "تم تسجيل الخروج.", updated: "تم الحفظ.",
    noEvents: "لا توجد إعلانات بعد — عودي قريباً.", membersTag: "للأعضاء"
  } : {
    badEmail: "Enter a valid email address.", shortPw: "Password must be at least 6 characters.",
    checkInbox: "Check your inbox to confirm your account, then come back and sign in.",
    resetSent: "Password reset link sent to your email.",
    welcome: "Welcome", signedOut: "Signed out.", updated: "Saved.",
    noEvents: "No announcements yet — check back soon.", membersTag: "Members"
  };

  function $(id) { return document.getElementById(id); }
  function msg(el, text, ok) { el.textContent = text; el.className = "auth-msg " + (ok ? "ok" : "err"); }
  function esc(t) { var d = document.createElement("div"); d.textContent = t == null ? "" : t; return d.innerHTML; }

  function waitDb(cb) {
    if (window.LM_DB) return cb(window.LM_DB);
    setTimeout(function () { waitDb(cb); }, 150);
  }

  waitDb(function (db) {
    var authView = $("auth-view"), memberView = $("member-view");

    function refresh() {
      db.auth.getSession().then(function (r) {
        var session = r.data && r.data.session;
        if (!session) { authView.style.display = ""; memberView.style.display = "none"; return; }
        authView.style.display = "none"; memberView.style.display = "";
        var email = session.user.email;
        var name = (session.user.user_metadata && session.user.user_metadata.full_name) || "";
        $("member-hello").textContent = T.welcome + (name ? ", " + name.split(" ")[0] : "") + " · " + email;
        db.from("profiles").select("role").eq("id", session.user.id).single().then(function (p) {
          var adminLink = $("admin-link");
          if (adminLink && p.data && p.data.role === "admin") adminLink.style.display = "";
        });
        db.from("events").select("*").eq("published", true)
          .order("created_at", { ascending: false }).limit(12)
          .then(function (ev) {
            var ul = $("member-events");
            if (!ul) return;
            if (ev.error || !ev.data || !ev.data.length) { ul.innerHTML = "<li><p>" + T.noEvents + "</p></li>"; return; }
            ul.innerHTML = ev.data.map(function (e) {
              var title = lang === "ar" ? (e.title_ar || e.title_en) : e.title_en;
              var body = lang === "ar" ? (e.body_ar || e.body_en) : e.body_en;
              var when = e.starts_on ? '<span class="when">' + esc(e.starts_on) + "</span>" : "";
              var tag = e.members_only ? '<span class="tag-members">' + T.membersTag + "</span>" : "";
              return "<li>" + when + "<h3>" + esc(title) + tag + "</h3><p>" + esc(body) + "</p></li>";
            }).join("");
          });
      });
    }

    $("form-signin").addEventListener("submit", function (e) {
      e.preventDefault();
      var m = $("signin-msg");
      db.auth.signInWithPassword({ email: $("si-email").value.trim(), password: $("si-pw").value })
        .then(function (r) { if (r.error) msg(m, r.error.message, false); else refresh(); });
    });

    $("form-signup").addEventListener("submit", function (e) {
      e.preventDefault();
      var m = $("signup-msg");
      var pw = $("su-pw").value;
      if (pw.length < 6) return msg(m, T.shortPw, false);
      db.auth.signUp({
        email: $("su-email").value.trim(), password: pw,
        options: { data: { full_name: $("su-name").value.trim() }, emailRedirectTo: location.origin + location.pathname }
      }).then(function (r) {
        if (r.error) msg(m, r.error.message, false);
        else if (r.data.session) refresh();
        else msg(m, T.checkInbox, true);
      });
    });

    $("btn-reset").addEventListener("click", function () {
      var m = $("signin-msg");
      var email = $("si-email").value.trim();
      if (!email) return msg(m, T.badEmail, false);
      db.auth.resetPasswordForEmail(email, { redirectTo: location.origin + location.pathname })
        .then(function (r) { msg(m, r.error ? r.error.message : T.resetSent, !r.error); });
    });

    $("btn-signout").addEventListener("click", function () {
      db.auth.signOut().then(refresh);
    });

    /* password recovery flow lands here with a session */
    db.auth.onAuthStateChange(function (event) {
      if (event === "PASSWORD_RECOVERY") {
        var np = prompt(lang === "ar" ? "كلمة المرور الجديدة (٦ أحرف على الأقل):" : "New password (min 6 characters):");
        if (np && np.length >= 6) db.auth.updateUser({ password: np });
      }
      refresh();
    });
    refresh();
  });
})();
