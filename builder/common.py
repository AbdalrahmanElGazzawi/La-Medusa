# La Medusa static site builder — shared templates & art
# Domain is a placeholder until decided; find-replace or edit here + rebuild.
DOMAIN = "https://lamedusadahab.com"

BRAND_EN = "La Medusa"
SUB_EN = "The Aerialist Shala"
BRAND_AR = "لا ميدوزا"
SUB_AR = "شالا الطيران"

NAV = [
    ("", {"en": "Home", "ar": "الرئيسية"}),
    ("classes/", {"en": "Classes", "ar": "الحصص"}),
    ("teacher-training/", {"en": "Teacher training", "ar": "تدريب المعلمين"}),
    ("retreats/", {"en": "Retreats", "ar": "الريتريتات"}),
    ("teachers/", {"en": "Teachers", "ar": "المعلمات"}),
    ("hammocks/", {"en": "Hammocks", "ar": "الأراجيح"}),
    ("accessibility/", {"en": "Every body flies", "ar": "كل جسدٍ يطير"}),
    ("contact/", {"en": "Contact", "ar": "تواصلي معنا"}),
]

ICON_WA = '''<svg class="wa-ic" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.87 9.87 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2zm0 18.02c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.03 8.03 0 0 1-1.23-4.25c0-4.43 3.6-8.03 8.03-8.03 4.43 0 8.03 3.6 8.03 8.03s-3.61 8.11-8.04 8.11zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.17.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28z"/></svg>'''

ART_JELLY = '''<svg viewBox="0 0 120 96" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M20 45 Q20 12 60 12 Q100 12 100 45 Z" fill="#EAF6F4"/><path d="M20 45 Q20 12 60 12 Q100 12 100 45" fill="none" stroke="#4CB1A7" stroke-width="2.5" stroke-linecap="round"/><path d="M32 48 Q28 62 34 78" fill="none" stroke="#846FB7" stroke-width="2.5" stroke-linecap="round"/><path d="M52 48 Q50 68 44 86" fill="none" stroke="#846FB7" stroke-width="2.5" stroke-linecap="round"/><path d="M70 48 Q72 66 78 82" fill="none" stroke="#846FB7" stroke-width="2.5" stroke-linecap="round"/><path d="M88 48 Q92 60 88 74" fill="none" stroke="#846FB7" stroke-width="2.5" stroke-linecap="round"/></svg>'''

ART_SILK = '''<svg viewBox="0 0 90 120" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M45 0 C30 40 62 60 45 120" fill="none" stroke="#846FB7" stroke-width="3" stroke-linecap="round" opacity="0.7"/><path d="M45 0 C58 42 30 64 45 118" fill="none" stroke="#59B8AF" stroke-width="3" stroke-linecap="round" opacity="0.7"/></svg>'''

def art_horizon(label_en_ar):
    return f'''<svg viewBox="0 0 1440 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label_en_ar}" preserveAspectRatio="xMidYMax slice">
<rect width="1440" height="300" fill="#FFFFFF"/>
<path d="M0 132 L180 92 L340 128 L470 74 L610 122 L760 88 L900 126 L1060 70 L1220 118 L1360 92 L1440 112" fill="none" stroke="#E5E0F2" stroke-width="3"/>
<path d="M0 150 L200 116 L360 148 L520 104 L680 144 L840 112 L1000 146 L1180 100 L1330 138 L1440 120 L1440 176 L0 176 Z" fill="#F1EEF8"/>
<circle cx="1120" cy="74" r="30" fill="#F6F0E3"/>
<path d="M716 0 Q722 96 728 0" fill="none" stroke="#846FB7" stroke-width="3.5"/>
<ellipse cx="722" cy="102" rx="42" ry="15" fill="#846FB7"/>
<circle cx="722" cy="80" r="8" fill="#6A57A6"/>
<path d="M690 106 Q722 130 754 106" fill="none" stroke="#6A57A6" stroke-width="4" stroke-linecap="round"/>
<rect x="0" y="176" width="1440" height="70" fill="#59B8AF"/>
<path d="M0 176 Q120 168 240 176 T480 176 T720 176 T960 176 T1200 176 T1440 176" fill="none" stroke="#4CB1A7" stroke-width="5"/>
<path d="M0 205 Q180 197 360 205 T720 205 T1080 205 T1440 205" fill="none" stroke="#7FCCC4" stroke-width="2.5" opacity="0.8"/>
<rect x="0" y="246" width="1440" height="54" fill="#EDE3CD"/>
<path d="M0 246 Q160 240 320 246 T640 246 T960 246 T1280 246 L1440 246" fill="none" stroke="#E2D4B4" stroke-width="3"/>
</svg>'''

def cocoon(fill):
    return f'''<svg class="cocoon-divider" viewBox="0 0 1440 70" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" aria-hidden="true"><path d="M0 70 C 360 0 1080 0 1440 70 Z" fill="{fill}"/></svg>'''

FONTS_EN = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500&family=Cormorant+Garamond:ital,wght@1,500&display=swap" rel="stylesheet">'''

FONTS_AR = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500&family=Cormorant+Garamond:ital,wght@1,500&display=swap" rel="stylesheet">'''


def page(slug, lang, title, desc, body, jsonld="", og_title=None):
    is_ar = lang == "ar"
    dirattr = "rtl" if is_ar else "ltr"
    prefix = "/ar" if is_ar else ""
    other_prefix = "" if is_ar else "/ar"
    fonts = FONTS_AR if is_ar else FONTS_EN
    brand1 = BRAND_AR if is_ar else BRAND_EN
    brand2 = SUB_AR if is_ar else SUB_EN
    lang_label = "English" if is_ar else "عربي"
    nav_items = ""
    for path, labels in NAV:
        href = f"{prefix}/{path}" if path else (prefix + "/" if is_ar else "/")
        current = ' aria-current="page"' if path == slug else ""
        nav_items += f'<li><a href="{href}"{current}>{labels[lang]}</a></li>'
    canonical = f"{DOMAIN}{prefix}/{slug}"
    alt_en = f"{DOMAIN}/{slug}"
    alt_ar = f"{DOMAIN}/ar/{slug}"
    switch_href = f"{other_prefix}/{slug}" if slug else (other_prefix + "/" if other_prefix else "/")
    nav_aria = "التنقل الرئيسي" if is_ar else "Main navigation"
    menu_aria = "فتح القائمة" if is_ar else "Open menu"
    skip = "تخطّي إلى المحتوى" if is_ar else "Skip to content"
    wa_aria = "تواصلي معنا عبر واتساب" if is_ar else "Chat with us on WhatsApp"
    footer = footer_html(lang, prefix)
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{dirattr}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="ar" href="{alt_ar}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title or title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.png">
<meta property="og:locale" content="{'ar_EG' if is_ar else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/assets/img/logo.png">
<link rel="apple-touch-icon" href="/assets/img/logo.png">
{fonts}
<link rel="stylesheet" href="/assets/css/main.css">
{jsonld}
</head>
<body>
<a class="skip-link" href="#main">{skip}</a>
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{prefix + '/' if prefix else '/'}" aria-label="{brand1} — {brand2}">
      <img src="/assets/img/logo.png" alt="" width="54" height="54">
      <span class="brand-name"><span class="bn-1">{brand1}</span><span class="bn-2">{brand2}</span></span>
    </a>
    <nav class="main-nav" aria-label="{nav_aria}"><ul>{nav_items}</ul></nav>
    <div style="display:flex;align-items:center;gap:10px">
      <a class="lang-switch" href="{switch_href}" lang="{'en' if is_ar else 'ar'}" dir="{'ltr' if is_ar else 'rtl'}">{lang_label}</a>
      <button class="nav-toggle" aria-expanded="false" aria-label="{menu_aria}"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
{footer}
<a class="wa-float" data-wa="general" href="#" aria-label="{wa_aria}"><svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.87 9.87 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2zm0 18.02c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.03 8.03 0 0 1-1.23-4.25c0-4.43 3.6-8.03 8.03-8.03 4.43 0 8.03 3.6 8.03 8.03s-3.61 8.11-8.04 8.11zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.17.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.22.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28z"/></svg></a>
<script src="/assets/js/config.js"></script>
<script src="/assets/js/main.js" defer></script>
</body>
</html>'''


def footer_html(lang, prefix):
    if lang == "ar":
        links = "".join(f'<li><a href="{prefix}/{p}">{l["ar"]}</a></li>' for p, l in NAV[1:])
        return f'''<footer class="site-footer">
<div class="container">
  <div class="footer-grid">
    <div class="footer-brand">
      <span class="brand-name"><span class="bn-1" style="font-size:24px">{BRAND_AR}</span><span class="bn-2">{SUB_AR}</span></span>
      <p>استوديو يوغا هوائية في العسلة، دهب — حيث تلتقي جبال سيناء بالبحر الأحمر.</p>
      <p class="footer-tagline">تحرّكي بجمال. اشعري بالحرية. حلّقي برشاقة.</p>
    </div>
    <div><h4>الاستوديو</h4><ul>{links}</ul></div>
    <div><h4>تابعينا</h4><ul>
      <li><a href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">@theaerialistshala</a></li>
      <li><a href="https://www.instagram.com/yogawith_mona/" target="_blank" rel="noopener">@yogawith_mona</a></li>
      <li><a href="https://www.instagram.com/profoundlytrue/" target="_blank" rel="noopener">@profoundlytrue</a></li>
      <li><a href="https://www.instagram.com/hammocksbymonashafei/" target="_blank" rel="noopener">@hammocksbymonashafei</a></li>
    </ul></div>
    <div><h4>احجزي</h4><ul>
      <li><a data-wa="general" href="#">واتساب +20 115 616 6225</a></li>
      <li><a href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">راسلينا "AERIAL" على إنستغرام</a></li>
      <li>العسلة، دهب، جنوب سيناء</li>
    </ul></div>
  </div>
  <div class="footer-bottom"><span>© 2026 لا ميدوزا · شالا الطيران — دهب، مصر</span><span>كل جسدٍ يطير.</span></div>
</div>
</footer>'''
    links = "".join(f'<li><a href="/{p}">{l["en"]}</a></li>' for p, l in NAV[1:])
    return f'''<footer class="site-footer">
<div class="container">
  <div class="footer-grid">
    <div class="footer-brand">
      <span class="brand-name"><span class="bn-1" style="font-size:24px">{BRAND_EN}</span><span class="bn-2">{SUB_EN}</span></span>
      <p>An aerial yoga studio in Assala, Dahab — where the Sinai mountains meet the Red Sea.</p>
      <p class="footer-tagline">Move beautifully. Feel freely. Fly gracefully.</p>
    </div>
    <div><h4>Studio</h4><ul>{links}</ul></div>
    <div><h4>Follow</h4><ul>
      <li><a href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">@theaerialistshala</a></li>
      <li><a href="https://www.instagram.com/yogawith_mona/" target="_blank" rel="noopener">@yogawith_mona</a></li>
      <li><a href="https://www.instagram.com/profoundlytrue/" target="_blank" rel="noopener">@profoundlytrue</a></li>
      <li><a href="https://www.instagram.com/hammocksbymonashafei/" target="_blank" rel="noopener">@hammocksbymonashafei</a></li>
    </ul></div>
    <div><h4>Book</h4><ul>
      <li><a data-wa="general" href="#">WhatsApp +20 115 616 6225</a></li>
      <li><a href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">DM "AERIAL" on Instagram</a></li>
      <li>Assala, Dahab, South Sinai</li>
    </ul></div>
  </div>
  <div class="footer-bottom"><span>© 2026 La Medusa · The Aerialist Shala — Dahab, Egypt</span><span>Every body flies.</span></div>
</div>
</footer>'''
