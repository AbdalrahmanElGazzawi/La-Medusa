# -*- coding: utf-8 -*-
# Arabic page bodies + metadata (RTL). Draft copy — to be reviewed by Reem before launch.
from common import ART_JELLY, ART_SILK, ICON_WA, art_horizon, cocoon, DOMAIN

CLASSES_AR = [
    ("تدفق هوائي", "فينياسا بقيادة النَفَس داخل الأرجوحة وخارجها — انسيابٌ وانحناءٌ وختامٌ رأساً على عقب.", "٥٠٠–٦٥٠", "كل المستويات", "sea"),
    ("مدخل إلى السيلك", "رحلتك الأولى في الهواء. تعرّفي على القماش، ابني الثقة، واختمي متأرجحةً في الشرنقة.", "٥٠٠", "مبتدئات", "lav"),
    ("هوائي استرخائي", "أوضاع بطيئة ومدعومة. الأرجوحة تحملك ليستطيع جهازك العصبي أن يرتاح.", "٥٠٠–٦٥٠", "كل المستويات", "sea"),
    ("مرونة الأرجوحة", "عمل عميق على الوركين والعمود الفقري والكتفين، والأرجوحة أداتك.", "٦٥٠", "كل المستويات", "lav"),
    ("هوائي للأطفال واليافعين", "لعبٌ وقوة وثقة في الهواء — بأمانٍ وإشرافٍ وفرح.", "٥٠٠–٦٥٠", "من ٦ إلى ١٥ سنة", "sand"),
    ("هوائي علاجي", "تخفيف ضغط لطيف وإطلاق موجّه لظهورٍ تجلس طويلاً خلف المكاتب.", "٥٠٠–٦٥٠", "كل المستويات", "sea"),
    ("سلسلة الهوب الهوائي", "فنٌّ وقوة على الليرا — سلسلة تصاعدية على عدة أسابيع.", "٥٠٠–٦٥٠", "تصاعدية", "lav"),
    ("سيلك متقدم", "تقنيات قماش متقدمة لمن اعتدن التحليق — لفّات وفنّ بلا سقطات.", "٥٠٠–٦٥٠", "متقدمات", "sea"),
    ("فينياسا وهاثا (على السجادة)", "حصص أرضية تبني النَفَس والأساس الذي تنمو منه ممارستك الهوائية.", "٥٠٠–٦٥٠", "كل المستويات", "sand"),
]

SCHEDULE_AR = [
    ("الأحد", "يين هوائي", "٧:٠٠ مساءً · كل المستويات"),
    ("الثلاثاء", "هوائي ١٠١", "٧:٠٠ مساءً · مناسب للمبتدئات"),
    ("الخميس", "يين هوائي", "٧:٠٠ مساءً · كل المستويات"),
    ("الجمعة", "هوائي ١٠١", "٩:٠٠ صباحاً · مناسب للمبتدئات"),
]

def class_cards(items):
    out = ""
    for name, desc, price, level, tint in items:
        art = {"sea": "background:var(--seafoam)", "lav": "background:var(--lavender)", "sand": "background:var(--sand-2)"}[tint]
        out += f'''<article class="card reveal">
<div class="card-art" style="{art}"></div>
<h3>{name}</h3>
<p>{desc}</p>
<div class="chip-row"><span class="chip">٩٠ دقيقة</span><span class="chip chip-lav">{level}</span></div>
<div class="price-tag">{price} ج.م <small>/ الحصة</small></div>
<a class="card-cta" data-wa="classes" data-book href="#">احجزي هذه الحصة ←</a>
</article>'''
    return out


HOME_BODY = f'''
<section class="hero">
  <div class="floaters" aria-hidden="true">
    <div class="floater floater-1">{ART_JELLY}</div>
    <div class="floater floater-2">{ART_SILK}</div>
    <div class="floater floater-3">{ART_JELLY}</div>
  </div>
  <div class="hero-inner">
    <p class="hero-kicker">يوغا هوائية · العسلة، دهب · جنوب سيناء</p>
    <h1>تحرّكي بجمال.<br>اشعري بالحرية. <span class="line-accent">حلّقي برشاقة.</span></h1>
    <p class="hero-sub">استوديو هوائي هادئ بين جبال سيناء والبحر الأحمر. تبدأ الحصص بتمددٍ لطيف، وتتصاعد إلى الانقلابات، وتُختم بتأرجحٍ داخل الشرنقة.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" data-wa="classes" data-book href="#">{ICON_WA} احجزي عبر واتساب</a>
      <a class="btn btn-ghost" href="/ar/classes/">اكتشفي الحصص</a>
    </div>
  </div>
  <div class="horizon">{art_horizon("رسم لممارِسة يوغا هوائية معلّقة فوق بحر دهب وصحرائها")}</div>
</section>
<div data-live-news class="container"></div>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="sec-kicker">الشالا</span>
        <h2>حيث تلتقي الصحراء بالبحر — وتلتقين أنتِ بالهواء</h2>
        <p class="sec-lead">لا ميدوزا هي استوديو اليوغا الهوائية في دهب. ممارستنا ناعمة عن قصد: لا سقطات ولا ثقافة «الحركات البهلوانية أولاً» — فقط النَفَس والقماش واكتشافٌ بطيء بأن جسدك قادر على التعلّق والانحناء والتحليق.</p>
        <p class="sec-lead">وتنتهي كل حصة بالطريقة نفسها: ملفوفةً في الأرجوحة، تتمايلين كقنديل بحرٍ في ماءٍ ساكن.</p>
        <a class="btn btn-ghost mt-2" href="/ar/teachers/">تعرّفي على معلّماتك</a>
      </div>
      <div class="photo-slot has-photo reveal" data-photo-slot="home_studio" style="min-height:380px"><img class="photo" src="/assets/img/photos/studio-aerialist.jpg" style="object-position:center 30%" alt="ممارِسة هوائية في وضعية كاملة تحت شعار لا ميدوزا المرسوم في الشالا" loading="lazy"></div>
    </div>
  </div>
</section>

{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">الحصص</span>
      <h2>حصص مصمّمة لكل المستويات — كبار وصغار</h2>
      <p class="sec-lead">حصص من ٩٠ دقيقة بين ٥٠٠ و٦٥٠ جنيهاً. مجموعات صغيرة، وعينا المعلّمة على كل جسد.</p>
    </div>
    <div class="card-grid">
      {class_cards(CLASSES_AR[:3])}
    </div>
    <p class="center mt-3"><a class="btn btn-sea" href="/ar/classes/">كل الحصص والجدول</a></p>
  </div>
</section>

{cocoon("#F1EEF8")}
<section class="section section-tint-lav">
  <div class="container">
    <div class="quote-band reveal">
      <blockquote>«كل جسدٍ مرحّبٌ به؛ نعدّل الوضعية على مقاس الإنسان.»</blockquote>
      <cite>المعيار الذي نُدرّس به كل حصة</cite>
      <p class="mt-2"><a class="btn btn-ghost" href="/ar/accessibility/">وعدنا بإتاحة الوصول — كل جسدٍ يطير</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">تدريب المعلمين</span>
      <h2>دورة تدريب معلمات اليوغا الهوائية — مثبتة لا موعودة</h2>
    </div>
    <div class="proof-row reveal">
      <div class="proof"><div class="p-num">٢</div><div class="p-label">دفعتان تخرّجتا — أبريل ٢٠٢٥ وأبريل ٢٠٢٦</div></div>
      <div class="proof"><div class="p-num">يوليو ٢٦</div><div class="p-label">الدفعة القادمة — التسجيل جارٍ الآن</div></div>
      <div class="proof"><div class="p-num">E-RYT 200</div><div class="p-label">بقيادة منى شافعي، YACEP</div></div>
      <div class="proof"><div class="p-num">سيناء</div><div class="p-label">الدورة المتخصصة لتدريب معلمي اليوغا الهوائية في سيناء</div></div>
    </div>
    <p class="center mt-3">
      <span class="badge-enrolling">دفعة يوليو ٢٠٢٦ — التسجيل جارٍ الآن</span><br><br>
      <a class="btn btn-primary" href="/ar/teacher-training/">اكتشفي التدريب</a>
    </p>
  </div>
</section>

{cocoon("#F6F0E3")}
<section class="section section-tint-sand">
  <div class="container">
    <div class="split">
      <div class="photo-slot has-photo reveal" data-photo-slot="retreat_home" style="min-height:340px"><img class="photo" src="/assets/img/photos/pergola-hammocks.jpg" alt="أراجيح هوائية ملوّنة معلّقة في الشالا المفتوحة" loading="lazy"></div>
      <div class="reveal">
        <span class="sec-kicker">الريتريتات</span>
        <h2>حلّقي حيث تنحدر الجبال إلى البحر</h2>
        <p class="sec-lead">أقمنا أول ريتريت لنا في ٢٠٢٥ — أيام من الممارسة الهوائية والنَفَس وماء البحر، بإقامةٍ لدى فنادق شريكة مرخّصة على شاطئ دهب.</p>
        <a class="btn btn-ghost mt-2" href="/ar/retreats/">الريتريتات والمواعيد القادمة</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="card reveal" style="padding:36px">
        <div class="card-art" style="background:var(--lavender)"></div>
        <h3>أراجيح منى شافعي</h3>
        <p>أراجيح هوائية مصنوعة يدوياً على مقاس حركتك — تصميم شخصي وألوان مخصصة، صناعة دهب. للممارسات وللاستوديوهات والفنادق.</p>
        <a class="card-cta" href="/ar/hammocks/">مشغل الأراجيح ←</a>
      </div>
      <div class="card reveal" style="padding:36px">
        <div class="card-art" style="background:var(--seafoam)"></div>
        <h3>مؤسِّستان، وشالا واحدة</h3>
        <p>منى شافعي (E-RYT 200، YACEP) تقود التدريب والريتريتات ومشغل الأراجيح. وريم أبو العلا (معتمدة من Yoga Alliance) تجعل الرحلة الأولى في الهواء آمنة ودافئة وصبورة.</p>
        <a class="card-cta" href="/ar/teachers/">تعرّفي على منى وريم ←</a>
      </div>
    </div>
  </div>
</section>


{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">الحياة في الشالا</span>
      <h2>حصص حقيقية، وناس حقيقيون، وتحليق حقيقي</h2>
      <p class="sec-lead">كل الصور أدناه التُقطت في استوديونا المفتوح في العسلة.</p>
    </div>
    <div class="gallery-grid reveal">
      <img class="g-wide" src="/assets/img/photos/group-shala.jpg" alt="مجموعة مبتهجة أمام شعار لا ميدوزا بعد الحصة" loading="lazy">
      <img src="/assets/img/photos/community-circle.jpg" alt="مجتمع الشالا في حلقة تحت الأقمشة" loading="lazy">
      <img src="/assets/img/photos/assisted-group.jpg" alt="طالبات يساعدن بعضهن في تمرين هوائي جماعي" loading="lazy">
      <img src="/assets/img/photos/inversion.jpg" alt="طالبة معلّقة رأساً على عقب في أرجوحة هوائية" loading="lazy">
      <img src="/assets/img/photos/partner-practice.jpg" alt="طالبتان تمارسان وضعية هوائية ثنائية" loading="lazy">
    </div>
    <p class="center mt-3"><a class="btn btn-ghost" href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">المزيد على إنستغرام — @theaerialistshala</a></p>
  </div>
</section>

<section class="section">
  <div class="container center">
    <div class="sec-head center reveal">
      <span class="sec-kicker">شاهدي</span>
      <h2>الشالا في حركة</h2>
    </div>
    <div class="ig-embed-wrap reveal">
      <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/DaVlvwAoZu4/" data-instgrm-version="14" style="margin:0 auto; max-width:540px; width:100%"></blockquote>
    </div>
  </div>
</section>
<script async src="https://www.instagram.com/embed.js"></script>

{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container center reveal">
    <h2>حلّقي معنا هذا الأسبوع</h2>
    <p class="sec-lead" style="max-width:560px;margin-left:auto;margin-right:auto">راسلينا على واتساب — أو أرسلي كلمة <strong>«AERIAL»</strong> إلى <a href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">@theaerialistshala</a> — وسنجد لك أرجوحة.</p>
    <div class="hero-ctas mt-2">
      <a class="btn btn-primary" data-wa="classes" href="#">{ICON_WA} واتساب +20 115 616 6225</a>
      <a class="btn btn-ghost" href="/ar/contact/">كل طرق التواصل</a>
    </div>
  </div>
</section>
'''

CLASSES_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">الحصص والجدول</span>
    <h1>حصص مصمّمة <span class="line-accent">لكل جسد</span></h1>
    <p class="ph-lead">حصص من ٩٠ دقيقة في أجواء هادئة ومجموعات صغيرة. الحجز المسبق مطلوب — راسلينا وسنحجز لك أرجوحتك.</p>
    <div class="hero-ctas"><a class="btn btn-primary" data-wa="classes" data-book href="#">{ICON_WA} احجزي حصة</a></div>
  </div>
  <div class="page-hero-band horizon">{art_horizon("ممارِسة يوغا هوائية فوق شاطئ دهب")}</div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head reveal">
      <span class="sec-kicker">القائمة</span>
      <h2>تسع طرق للتحليق</h2>
      <p class="sec-lead">كل الحصص الهوائية تشمل شرحاً كاملاً للسلامة، ومناطق هبوط مبطّنة، وتجهيزات تفحصها المعلّمة يومياً. الحصص بين ٥٠٠ و٦٥٠ جنيهاً للفرد (٩٠ دقيقة)، ويُؤكَّد سعر كل حصة عند الحجز.</p>
    </div>
    <div class="card-grid">{class_cards(CLASSES_AR)}</div>
    <div class="note-soft mt-3">يُؤكَّد الجدول والأسعار عند الحجز — وتُعلن أسعار المقيمين والزوّار وباقات الحصص عبر واتساب. أماكن بالتسعير التدرّجي متاحة في كل حصة: اطّلعي على <a href="/ar/accessibility/">وعد الإتاحة</a>.</div>
  </div>
</section>

{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">هذا الأسبوع</span>
      <h2>جدول الأسبوع</h2>
      <p class="sec-lead" data-schedule-status>يحدّث الاستوديو هذا الجدول مباشرةً — وتُعلن التغييرات أيضاً على واتساب وقصص إنستغرام.</p>
    </div>
    <div class="schedule-wrap reveal">
      <table class="schedule">
        <caption class="visually-hidden">جدول الحصص الأسبوعي</caption>
        <thead><tr><th scope="col">اليوم</th><th scope="col">الحصة</th><th scope="col">الوقت والمستوى</th></tr></thead>
        <tbody data-live-schedule>
          {"".join(f'<tr><th scope="row" class="cls">{d}</th><td class="cls">{c}</td><td><span class="meta">{m}</span></td></tr>' for d, c, m in SCHEDULE_AR)}
        </tbody>
      </table>
    </div>
    <p class="center mt-3"><a class="btn btn-primary" data-wa="classes" data-book href="#">{ICON_WA} اطلبي جدول هذا الأسبوع</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <h3>حصتك الأولى</h3>
        <ul class="checklist mt-1">
          <li>احضري قبل الموعد بربع ساعة للترحيب واستمارة الصحة.</li>
          <li>ارتدي ليغنغز وقميصاً يغطي الإبطين — حروق القماش حقيقية.</li>
          <li>بلا خواتم أو ساعات أو سحّابات أو زيوت؛ والشعر مربوط.</li>
          <li>كُلي خفيفاً — لا طعام ثقيل قبل الانقلاب بساعتين.</li>
          <li>أنتِ من يتحكم في كل نزول. لا شيء يُفرض عليك أبداً.</li>
        </ul>
      </div>
      <div class="reveal">
        <h3>الأطفال يطيرون أيضاً</h3>
        <p class="sec-lead">حصص الأطفال واليافعين تبني القوة والتركيز والفرح الجريء — بمعايير السلامة نفسها في حصص الكبار.</p>
        <a class="btn btn-ghost mt-2" data-wa="kids" href="#">اسألي عن حصص الأطفال</a>
      </div>
    </div>
  </div>
</section>
'''

AYTTC_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="badge-enrolling">دفعة يوليو ٢٠٢٦ — التسجيل جارٍ الآن</span>
    <h1 class="mt-2">كوني معلّمة يوغا هوائية — <span class="line-accent">في دهب</span></h1>
    <p class="ph-lead">دورة AYTTC هي التدريب المتخصص لمعلمي اليوغا الهوائية في سيناء: دفعات صغيرة، وتدريس حقيقي، ومنهج مبني على دليلنا الخاص «Pose &amp; Practice Manual».</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" data-wa="ayttc" href="#">{ICON_WA} احجزي مكانك</a>
      <a class="btn btn-ghost" href="#curriculum">اطّلعي على المنهج</a>
    </div>
  </div>
  <div class="page-hero-band horizon">{art_horizon("تدريب هوائي فوق أفق دهب")}</div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">سجل الإنجاز</span>
      <h2>مثبتة، لا موعودة</h2>
    </div>
    <div class="proof-row reveal">
      <div class="proof"><div class="p-num">أبريل ٢٥</div><div class="p-label">الدفعة الأولى تخرّجت</div></div>
      <div class="proof"><div class="p-num">أبريل ٢٦</div><div class="p-label">الدفعة الثانية تخرّجت</div></div>
      <div class="proof"><div class="p-num">يوليو ٢٦</div><div class="p-label">الدفعة الثالثة — التسجيل جارٍ</div></div>
      <div class="proof"><div class="p-num">صغيرة</div><div class="p-label">دفعات صغيرة — الجميع يُدرّس والجميع يُرى</div></div>
    </div>
    <div class="two-col mt-3">
      <div class="photo-slot has-photo reveal" data-photo-slot="ayttc_2025"><img class="photo" src="/assets/img/photos/practice-assist.jpg" alt="معلّمة تقدّم تعديلاً يدوياً أثناء الممارسة الهوائية" loading="lazy"></div>
      <div class="photo-slot has-photo reveal" data-photo-slot="ayttc_2026"><img class="photo" src="/assets/img/photos/teaching-spot.jpg" alt="طالبات يتابعن معلّمة وهي تساند انقلاباً في الاستوديو" loading="lazy"></div>
    </div>
  </div>
</section>

{cocoon("#F1EEF8")}
<section class="section section-tint-lav" id="curriculum">
  <div class="container">
    <div class="sec-head reveal">
      <span class="sec-kicker">المنهج</span>
      <h2>ماذا ستتعلمين</h2>
      <p class="sec-lead">منهج مبني على دليل لا ميدوزا وبقيادة منى شافعي (E-RYT 200، YACEP) — تدريب يُحتسب ضمن ساعات التعليم المستمر لدى Yoga Alliance.</p>
    </div>
    <ul class="timeline reveal">
      <li><span class="tl-when">الوحدة ١</span><h3>أساسيات التحليق</h3><p>نَسَب الأرجوحة الهوائية، وطريقة لا ميدوزا، والمبادئ الجسدية-الحسية لممارسةٍ تُهدّئ وهي تُقوّي.</p></li>
      <li><span class="tl-when">الوحدة ٢</span><h3>التجهيزات والسلامة</h3><p>معاملات الأمان الهندسية، ومعايير المعدات، وجولات الفحص اليومية والشهرية — قواعد لا تنازل عنها.</p></li>
      <li><span class="tl-when">الوحدة ٣</span><h3>الأسانا في الهواء</h3><p>مكتبة الوضعيات كاملة: الدخول والخروج والمساندة وموانع الاستخدام — والقاعدة الحاسمة: الطالبة تتحكم دائماً في النزول.</p></li>
      <li><span class="tl-when">الوحدة ٤</span><h3>تدريسٌ لكل جسد</h3><p>عدّلي الوضعية على مقاس الإنسان: تكييفات لأنواع الأجسام والقدرات والإصابات والمخاوف. هذا صلب المنهج هنا، لا هامشه.</p></li>
      <li><span class="tl-when">الوحدة ٥</span><h3>التسلسل والشرنقة</h3><p>صمّمي رحلات من ٩٠ دقيقة تبدأ بلطف، وتبلغ ذروتها بأمان، وتُنزل الجميع إلى السكينة.</p></li>
      <li><span class="tl-when">الوحدة ٦</span><h3>التطبيق العملي</h3><p>طالبات حقيقيات وملاحظات يومية — تتخرجين وقد درّستِ فعلاً.</p></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <h3>لمن هذه الدورة</h3>
        <ul class="checklist mt-1">
          <li>معلمات يوغا يُضفن تخصصاً هوائياً معتمداً.</li>
          <li>ممارسات ملتزمات مستعدات لتدريس حصتهن الأولى.</li>
          <li>محترفات الحركة — راقصات، أخصائيات علاج طبيعي، مدربات فري دايفينغ.</li>
          <li>لا يُشترط الوقوف على اليدين. تُشترط الممارسة المنتظمة.</li>
        </ul>
      </div>
      <div class="reveal">
        <h3>التسجيل — يوليو ٢٠٢٦</h3>
        <p class="sec-lead">الأماكن محدودة للحفاظ على صغر الدفعة. عربونٌ قابل للاسترداد يحجز مكانك؛ وتصلك الرسوم وخطط الدفع وملف المعلومات الكامل عبر واتساب.</p>
        <a class="btn btn-primary mt-2" data-wa="ayttc" href="#">{ICON_WA} اطلبي ملف المعلومات</a>
      </div>
    </div>
    <div class="note-soft mt-3">تتخرج المتدربات ومعهن دليل الوضعيات والممارسة، وشهادة تدريس من لا ميدوزا، وساعات تعليم مستمر مع معلّمتنا المعتمدة YACEP. اسألينا كيف يُحتسب التدريب في ملفك لدى Yoga Alliance.</div>
  </div>
</section>
'''

RETREATS_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">الريتريتات</span>
    <h1>أيام من الهواء والنَفَس <span class="line-accent">وماء البحر</span></h1>
    <p class="ph-lead">ريتريتات يوغا هوائية حيث تنحدر صحراء سيناء إلى البحر الأحمر — تحليق في الصباح، وبحرٌ في الظهيرة، وشرنقة عند الغروب.</p>
    <div class="hero-ctas"><a class="btn btn-primary" data-wa="retreat" href="#">{ICON_WA} انضمي لقائمة الريتريت</a></div>
  </div>
  <div class="page-hero-band horizon">{art_horizon("مشهد ريتريت: ممارِسة فوق البحر عند الغروب")}</div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="sec-kicker">٢٠٢٥ — أُنجز</span>
        <h2>أول ريتريت لنا — أُنجز</h2>
        <p class="sec-lead">أسبوعٌ من الممارسة الهوائية والمرونة وصباحات دهب البطيئة وبعد الظهر الطويل عند البحر. والنسخة القادمة تبني على كل ما تعلمناه.</p>
        <p class="sec-lead">الإقامة لدى فنادق شريكة مرخّصة على شاطئ دهب — تنامين قانونياً ومريحةً وعلى خطواتٍ من الماء.</p>
      </div>
      <div class="photo-slot has-photo reveal" data-photo-slot="retreat_2025" style="min-height:360px"><img class="photo" src="/assets/img/photos/restorative.jpg" alt="طالبات في وضعية استرخائية مدعومة" loading="lazy"></div>
    </div>
  </div>
</section>

{cocoon("#F6F0E3")}
<section class="section section-tint-sand">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">شكل اليوم في الريتريت</span>
      <h2>الإيقاع</h2>
    </div>
    <div class="card-grid reveal">
      <article class="card"><div class="card-art" style="background:var(--seafoam)"></div><h3>الصباح</h3><p>تمارين نَفَس مع الشروق وممارسة هوائية كاملة قبل الحر — ضوء الصحراء يقوم بنصف التدريس.</p></article>
      <article class="card"><div class="card-art" style="background:var(--lavender)"></div><h3>بعد الظهر</h3><p>وقت حر في عاصمة الفري دايفينغ العالمية: الشعاب، رحلات البلو هول، ساعات المقاهي، مساج، أو لا شيء إطلاقاً.</p></article>
      <article class="card"><div class="card-art" style="background:var(--sand-2)"></div><h3>الغروب</h3><p>هوائي استرخائي ثم الشرنقة والجبال تتحول إلى البنفسجي. وعشاء جماعي تحت النجوم.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <h3>المواعيد القادمة</h3>
        <p class="sec-lead">الريتريت القادم مخطط له في نافذة الموسم (أكتوبر–أبريل). تُعلن المواعيد والأسعار الدولية بالدولار واليورو وأماكن الحجز المبكر لقائمة واتساب أولاً.</p>
        <a class="btn btn-primary mt-2" data-wa="retreat" href="#">{ICON_WA} اعرفي المواعيد والأسعار أولاً</a>
        <p class="mt-1" style="font-size:14px"><a href="/ar/inquire/?topic=retreat">تفضلين الكتابة؟ أرسلي استفسار ريتريت ←</a></p>
      </div>
      <div class="reveal">
        <h3>معلومات مفيدة</h3>
        <ul class="checklist mt-1">
          <li>كل المستويات مرحّب بها — حتى من لم تحلّق من قبل.</li>
          <li>فنادق شريكة مرخّصة تتولى الإقامة.</li>
          <li>مجموعات صغيرة عن قصد.</li>
          <li>المسافرات المنفردات مرحّبٌ بهن بدفء.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''

TEACHERS_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">المعلمات</span>
    <h1>مؤسِّستان، <span class="line-accent">وشالا واحدة</span></h1>
    <p class="ph-lead">لا ميدوزا أسّستها ودرّست فيها وخاطت أراجيحها امرأتان تؤمنان بأن الهواء حقٌّ لكل جسد.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="teacher-grid">
      <article class="teacher reveal">
        <div class="photo-slot" role="img" aria-label="مكان صورة: منى شافعي" data-photo-slot="teacher_mona">{ART_SILK}<span class="ps-label">مكان صورة — منى شافعي</span></div>
        <div class="teacher-body">
          <h3>منى شافعي</h3>
          <p class="t-creds">E-RYT 200 · YACEP · مؤسِّسة</p>
          <p>رئيسة التدريب والمنتجات. تقود منى دورة تدريب المعلمات AYTTC (دفعتا أبريل ٢٠٢٥ وأبريل ٢٠٢٦)، وتصمم الريتريتات، وتدرّس مرونة الأرجوحة — وتصنع الأراجيح بنفسها تحت اسم <a href="/ar/hammocks/">أراجيح منى شافعي</a>. تمتد ممارستها إلى علاج تشي ني تسانغ.</p>
          <p class="mt-1"><a href="https://www.instagram.com/yogawith_mona/" target="_blank" rel="noopener">@yogawith_mona</a></p>
        </div>
      </article>
      <article class="teacher reveal">
        <div class="photo-slot" role="img" aria-label="مكان صورة: ريم أبو العلا" data-photo-slot="teacher_reem">{ART_SILK}<span class="ps-label">مكان صورة — ريم أبو العلا</span></div>
        <div class="teacher-body">
          <h3>ريم أبو العلا</h3>
          <p class="t-creds">معلمة هوائية معتمدة من Yoga Alliance · شريكة مؤسِّسة</p>
          <p>رئيسة الاستوديو والمجتمع. تدرّس ريم اليوغا الهوائية والسيلك بإرشادٍ دافئ وصبور يجعل المبتدئات يشعرن بأنهن محمولات — حرفياً. هي صوت الشالا ثنائي اللغة، وفنانتها، والسبب في أن المجتمع يشبه عائلة.</p>
          <p class="mt-1"><a href="https://www.instagram.com/profoundlytrue/" target="_blank" rel="noopener">@profoundlytrue</a></p>
        </div>
      </article>
    </div>
  </div>
</section>


<section class="section">
  <div class="container">
    <div class="photo-slot has-photo reveal" style="min-height:420px"><img class="photo" src="/assets/img/photos/group-shala.jpg" alt="معلّمات وطالبات أمام جدار لا ميدوزا" loading="lazy"></div>
  </div>
</section>
{cocoon("#F1EEF8")}
<section class="section section-tint-lav">
  <div class="container">
    <div class="quote-band reveal">
      <blockquote>«هدوءٌ عن قصد: نبدأ بتمددٍ لطيف، ونتصاعد إلى الانقلابات، ونختم بشرنقةٍ تتمايل.»</blockquote>
      <cite>طريقة لا ميدوزا</cite>
      <p class="mt-2"><a class="btn btn-primary" data-wa="classes" href="#">{ICON_WA} خذي حصة معنا</a></p>
    </div>
  </div>
</section>
'''

HAMMOCKS_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">أراجيح منى شافعي</span>
    <h1>أراجيح مصنوعة يدوياً، على مقاس <span class="line-accent">حركتك</span></h1>
    <p class="ph-lead">كل أرجوحة من لا ميدوزا تقصّها منى وتخيطها في دهب — منسوجة من قطنٍ طبيعي بنسبة ٧٠٪، بتصميم شخصي وألوان مخصصة، لممارسةٍ حقيقية.</p>
    <div class="hero-ctas"><a class="btn btn-primary" data-wa="hammocks" href="#">{ICON_WA} اطلبي الكتالوج</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="card-grid">
      <article class="card reveal"><div class="card-art" style="background:var(--seafoam)"></div><h3>لممارستك</h3><p>أرجوحة بألوانك، على مقاس طولك وسقفك — مع إرشاد صادق لتركيبها بأمان في بيتك.</p><a class="card-cta" data-wa="hammocks" href="#">اطلبي أرجوحتك ←</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--lavender)"></div><h3>للاستوديوهات والفنادق</h3><p>أطقم جملة للاستوديوهات وأماكن الريتريت والفنادق في مصر والمنطقة — مع إرشادات التركيب في كل طلب.</p><a class="card-cta" data-wa="partner" href="#">استفسار جملة ←</a><br><a class="card-cta" href="/ar/inquire/?topic=hammocks">أو أرسلي استفساراً مكتوباً ←</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--sand-2)"></div><h3>مصنوعة لتُوثَق بها</h3><p>نفس القماش ومعايير المعدات المصنّفة التي نعلّق بها طالباتنا — لأننا نفعل ذلك كل يوم في الشالا.</p><a class="card-cta" href="/ar/accessibility/">معايير السلامة ←</a></article>
    </div>
    <div class="two-col mt-3">
      <div class="photo-slot has-photo reveal" data-photo-slot="hammocks_fabric"><img class="photo" src="/assets/img/photos/fabric-yellow.jpg" alt="أراجيح صفراء مصنوعة يدوياً على جدار أزرق" loading="lazy"></div>
      <div class="photo-slot has-photo reveal" data-photo-slot="hammocks_atelier"><img class="photo" src="/assets/img/photos/brand-tote.jpg" alt="حقيبة تحمل شعار أراجيح منى شافعي" loading="lazy"></div>
    </div>
    <div class="note-soft mt-3">الأسعار والألوان المتاحة حالياً في كتالوج واتساب — أرسلي كلمة <strong>«HAMMOCKS»</strong> وسترسل لك منى الكتالوج. تابعي <a href="https://www.instagram.com/hammocksbymonashafei/" target="_blank" rel="noopener">@hammocksbymonashafei</a> للتشكيلات الجديدة.</div>
  </div>
</section>
'''

ACCESS_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">الوعد</span>
    <h1>كل جسدٍ <span class="line-accent">يطير</span></h1>
    <p class="ph-lead">«كل جسدٍ مرحّبٌ به؛ نعدّل الوضعية على مقاس الإنسان» ليست شعاراً أضفناه — بل المعيار الذي بُنيت عليه الشالا. هذا ما يعنيه عملياً، منشوراً لتحاسبونا عليه.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <ul class="timeline reveal">
      <li class="tl-done"><span class="tl-when">قائم الآن</span><h3>معيار التدريس لكل جسد</h3><p>تكييف الوضعيات لنوع الجسم والقدرة والإصابة والخوف جزء أساسي من كل حصة ومن منهج تدريب المعلمات — وليس فكرة لاحقة.</p></li>
      <li class="tl-done"><span class="tl-when">قائم الآن</span><h3>كل شيء بلغتين</h3><p>استمارات ولافتات وأدلة وحصص بالعربية والإنجليزية. نصف مجتمعنا محلي؛ والاحترام هو ما يُبقي الناس.</p></li>
      <li class="tl-now"><span class="tl-when">الربع الأخير ٢٠٢٦</span><h3>التسعير التدرّجي</h3><p>ثلاث فئات تختارينها بنفسك — داعمة للمجتمع، قياسية، مدعومة — دون طلب أي إثبات، أبداً. ليبقى أهل البلد في الحصة وسط اقتصادٍ سياحي.</p></li>
      <li class="tl-now"><span class="tl-when">الربع الأخير ٢٠٢٦</span><h3>مسار الحمل والتعافي</h3><p>الحصص الجماعية غير مناسبة أثناء الحمل، لذلك نقدم عملاً خاصاً مكيّفاً بموافقة طبية — ومساراً للتعافي بعد الإصابة بخطابٍ من طبيبك.</p></li>
      <li><span class="tl-when">الربع الأول ٢٠٢٧</span><h3>تدقيق الوصول وحصة هادئة</h3><p>تدقيق المدخل والحمّام ووسائل الصعود؛ صيغ أرجوحة منخفضة لمحدودية الحركة؛ وحصة أسبوعية هادئة منخفضة المؤثرات الحسية.</p></li>
      <li><span class="tl-when">٢٠٢٧</span><h3>هوائي مُكيَّف</h3><p>برنامج هوائي لمستخدمات الكراسي المتحركة على غرار برامج عالمية مثبتة — سيلك لتخفيف ضغط العمود الفقري، وبروتوكولات مساعدة مدرّبة، وجلسة شهرية للبداية — ونطمح أن يكون الأول من نوعه في مصر.</p></li>
    </ul>
  </div>
</section>

{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container">
    <div class="sec-head reveal">
      <span class="sec-kicker">السلامة هي العلامة</span>
      <h2>قواعد لا نتنازل عنها</h2>
      <p class="sec-lead">اليوغا الهوائية آمنة كما الطيران آمن: بفضل الأنظمة، لا الحظ.</p>
    </div>
    <div class="card-grid reveal">
      <article class="card"><div class="card-art" style="background:var(--seafoam)"></div><h3>تجهيزات مهندَسة</h3><p>معاملات أمان من ٥:١ إلى ١٠:١، ومثبّتان مستقلان معتمدان هندسياً لكل نقطة (≥٥٠٠ كغم لكل منهما)، ومعدات مصنّفة للتسلق فقط.</p></article>
      <article class="card"><div class="card-art" style="background:var(--lavender)"></div><h3>فحص يومي</h3><p>تختبر المعلمة حمولة كل أرجوحة يومياً؛ وفحوص شهرية موثّقة؛ ويُستبعد القماش والمعدات عند أول علامة تآكل.</p></article>
      <article class="card"><div class="card-art" style="background:var(--sand-2)"></div><h3>القاعدة الحاسمة</h3><p>لا انقلاب أعلى من الوقوف. لا سقطات ولا تأرجح تحت الحمل. الطالبة تتحكم دائماً في النزول.</p></article>
      <article class="card"><div class="card-art" style="background:var(--seafoam)"></div><h3>فحص قبل التحليق</h3><p>استمارة صحية لكل طالبة جديدة — الحمل، ضغط الدم، الجلوكوما، الجراحات الحديثة، الدوار — وصراحة كاملة حول متى لا يجب الانقلاب.</p></article>
      <article class="card"><div class="card-art" style="background:var(--lavender)"></div><h3>جاهزات لأي طارئ</h3><p>إسعافات أولية وإنعاش قلبي رئوي محدَّثان لكل المعلمات، ومناطق هبوط مبطّنة تحت كل أرجوحة، وبروتوكولات طوارئ واضحة.</p></article>
      <article class="card"><div class="card-art" style="background:var(--sand-2)"></div><h3>إن كان في الأمر شك</h3><p>…فالحصة لا تطير. بهذه البساطة.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container center reveal">
    <h2>غير متأكدة أن الهوائي يناسبك؟</h2>
    <p class="sec-lead" style="max-width:560px;margin:16px auto 0">هذه الصفحة كُتبت لك تحديداً. أخبرينا عن جسدك، وسنخبرك بصدق كيف يمكن أن تبدو حصتك الأولى.</p>
    <div class="hero-ctas mt-2"><a class="btn btn-primary" data-wa="access" href="#">{ICON_WA} اسألينا أي شيء</a></div>
  </div>
</section>
'''

CONTACT_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">تواصلي معنا</span>
    <h1>تجديننا حيث تلتقي الجبال <span class="line-accent">بالبحر</span></h1>
    <p class="ph-lead">كل شيء يمر عبر واتساب — الحجز والأسئلة وتدريب المعلمات وطلبات الأراجيح. رقم واحد، وبشرٌ حقيقيون.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="card-grid">
      <article class="card reveal"><div class="card-art" style="background:var(--seafoam)"></div><h3>احجزي حصة</h3><p>راسلينا وسنرسل جدول هذا الأسبوع ونحجز لك أرجوحتك.</p><a class="btn btn-primary" data-wa="classes" href="#">{ICON_WA} احجزي حصة</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--lavender)"></div><h3>تدريب المعلمات</h3><p>دفعة يوليو ٢٠٢٦ قيد التسجيل — اطلبي ملف المعلومات وتفاصيل العربون.</p><a class="btn btn-primary" data-wa="ayttc" href="#">{ICON_WA} ملف معلومات AYTTC</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--sand-2)"></div><h3>الريتريتات</h3><p>انضمي إلى القائمة التي تعرف المواعيد وأسعار الحجز المبكر أولاً.</p><a class="btn btn-primary" data-wa="retreat" href="#">{ICON_WA} قائمة الريتريت</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--seafoam)"></div><h3>الأراجيح</h3><p>اطلبي أرجوحة مخصصة أو اسألي عن أسعار الجملة لاستوديوهك أو فندقك.</p><a class="btn btn-primary" data-wa="hammocks" href="#">{ICON_WA} كتالوج الأراجيح</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--lavender)"></div><h3>الشراكات والفعاليات</h3><p>فعاليات الشركات، المهرجانات، حصص في مقرّكم، وتعاونات العلامات.</p><a class="btn btn-primary" data-wa="partner" href="#">{ICON_WA} كوني شريكاً</a><p class="mt-1" style="font-size:13.5px"><a href="/ar/inquire/?topic=corporate">أو أرسلي استفساراً مكتوباً ←</a></p></article>
      <article class="card reveal"><div class="card-art" style="background:var(--sand-2)"></div><h3>تفضلين إنستغرام؟</h3><p>أرسلي كلمة <strong>«AERIAL»</strong> إلى @theaerialistshala وسنتولى الباقي.</p><a class="btn btn-ghost" href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">افتحي إنستغرام</a></article>
    </div>

    <div class="two-col mt-3">
      <div class="reveal">
        <h3>الاستوديو</h3>
        <p class="sec-lead">لا ميدوزا · شالا الطيران<br>العسلة، دهب، جنوب سيناء، مصر</p>
        <p class="sec-lead">واتساب: <a data-wa="general" href="#">+20 115 616 6225</a><br>
        إنستغرام: <a href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">@theaerialistshala</a></p>
        <p class="sec-lead"><a href="https://maps.google.com/?q=Assala,+Dahab,+South+Sinai,+Egypt" target="_blank" rel="noopener">افتحي في خرائط غوغل ←</a></p>
      </div>
      <div class="reveal">
        <h3>قبل وصولك</h3>
        <ul class="checklist mt-1">
          <li>الحجز المسبق مطلوب — نحافظ على صغر المجموعات.</li>
          <li>الطالبات الجدد يصلن قبل الموعد بربع ساعة لاستمارة الصحة.</li>
          <li>الجدول الأسبوعي الفعلي يُنشر على واتساب وقصص إنستغرام.</li>
          <li>عربي أو إنجليزي — أيهما يشبه بيتك.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''

HOME_JSONLD = f'''<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "لا ميدوزا · شالا الطيران",
  "alternateName": "La Medusa · The Aerialist Shala",
  "description": "استوديو يوغا هوائية في العسلة، دهب، مصر. حصص لكل المستويات، تدريب معلمين، ريتريتات، وأراجيح مصنوعة يدوياً.",
  "url": "{DOMAIN}/ar/",
  "telephone": "+201156166225",
  "address": {{ "@type": "PostalAddress", "addressLocality": "Dahab", "addressRegion": "South Sinai", "addressCountry": "EG", "streetAddress": "Assala" }},
  "geo": {{ "@type": "GeoCoordinates", "latitude": 28.509, "longitude": 34.513 }},
  "sameAs": ["https://www.instagram.com/theaerialistshala/"],
  "priceRange": "EGP 500–650"
}}</script>'''

PAGES = {
    "": {
        "title": "لا ميدوزا · شالا الطيران — يوغا هوائية في دهب، مصر",
        "desc": "يوغا هوائية في دهب: حصص لكل المستويات (كبار وأطفال)، تدريب معلمي يوغا هوائية في مصر، ريتريتات على البحر الأحمر، وأراجيح مصنوعة يدوياً. احجزي عبر واتساب.",
        "body": HOME_BODY,
        "jsonld": HOME_JSONLD,
    },
    "classes/": {
        "title": "حصص اليوغا الهوائية والجدول في دهب — لا ميدوزا",
        "desc": "حصص يوغا هوائية في دهب من ٥٠٠ إلى ٦٥٠ جنيهاً: تدفق هوائي، سيلك، استرخائي، أطفال ويافعون، هوب والمزيد. حصص ٩٠ دقيقة بمجموعات صغيرة.",
        "body": CLASSES_BODY,
    },
    "teacher-training/": {
        "title": "تدريب معلمي اليوغا الهوائية في مصر — AYTTC يوليو ٢٠٢٦ | لا ميدوزا دهب",
        "desc": "دورة AYTTC لتدريب معلمي اليوغا الهوائية في دهب، مصر. دفعتا أبريل ٢٠٢٥ و٢٠٢٦ تخرّجتا — التسجيل جارٍ لدفعة يوليو ٢٠٢٦. بقيادة منى شافعي E-RYT 200.",
        "body": AYTTC_BODY,
    },
    "retreats/": {
        "title": "ريتريتات يوغا هوائية في دهب، مصر — لا ميدوزا",
        "desc": "ريتريتات يوغا هوائية على البحر الأحمر: تحليق صباحي، غروب يجمع الصحراء بالبحر، وفنادق شريكة مرخّصة. اكتمل ريتريت ٢٠٢٥ — انضمي لقائمة المواعيد القادمة.",
        "body": RETREATS_BODY,
    },
    "teachers/": {
        "title": "معلّماتنا — منى شافعي وريم أبو العلا | لا ميدوزا دهب",
        "desc": "تعرّفي على مؤسِّستَي لا ميدوزا: منى شافعي (E-RYT 200، YACEP، قائدة تدريب المعلمين) وريم أبو العلا (معلمة هوائية وسيلك معتمدة).",
        "body": TEACHERS_BODY,
    },
    "hammocks/": {
        "title": "أراجيح منى شافعي — أراجيح هوائية يدوية الصنع، دهب",
        "desc": "أراجيح يوغا هوائية مصنوعة يدوياً في دهب — تصميم شخصي، ألوان مخصصة، وجملة للاستوديوهات والفنادق. اطلبي عبر كتالوج واتساب.",
        "body": HAMMOCKS_BODY,
    },
    "accessibility/": {
        "title": "كل جسدٍ يطير — وعد الإتاحة | لا ميدوزا دهب",
        "desc": "تسعير تدرّجي، هوائي مُكيَّف، مسارات حمل وتعافٍ، حصص بلغتين، ومعايير سلامة منشورة. وعد لا ميدوزا بإتاحة الوصول، مكتوباً.",
        "body": ACCESS_BODY,
    },
    "contact/": {
        "title": "التواصل والحجز — لا ميدوزا · شالا الطيران، دهب",
        "desc": "احجزي اليوغا الهوائية في دهب عبر واتساب +20 115 616 6225 أو راسلي 'AERIAL' على إنستغرام. حصص وتدريب معلمين وريتريتات وأراجيح وشراكات.",
        "body": CONTACT_BODY,
    },
}


ACCOUNT_BODY_AR = '''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">الأعضاء</span>
    <h1>حسابك في <span class="line-accent">الشالا</span></h1>
    <p class="ph-lead">سجّلي الدخول لرؤية الجدول المباشر وإعلانات الأعضاء ومواعيد الريتريت قبل الجميع.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div id="auth-view">
      <div class="two-col" style="max-width:940px;margin:0 auto">
        <div class="auth-card">
          <h3>تسجيل الدخول</h3>
          <form id="form-signin" class="mt-1">
            <div class="field"><label for="si-email">البريد الإلكتروني</label><input id="si-email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="si-pw">كلمة المرور</label><input id="si-pw" type="password" autocomplete="current-password" required></div>
            <button class="btn btn-primary btn-block" type="submit">دخول</button>
            <div id="signin-msg" class="auth-msg" role="status"></div>
          </form>
          <p class="auth-alt"><button id="btn-reset" class="btn btn-ghost btn-sm" type="button">نسيتِ كلمة المرور؟</button></p>
        </div>
        <div class="auth-card">
          <h3>جديدة هنا؟ أنشئي حساباً</h3>
          <form id="form-signup" class="mt-1">
            <div class="field"><label for="su-name">اسمك</label><input id="su-name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="su-email">البريد الإلكتروني</label><input id="su-email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="su-pw">كلمة المرور (٦ أحرف على الأقل)</label><input id="su-pw" type="password" autocomplete="new-password" required></div>
            <button class="btn btn-sea btn-block" type="submit">إنشاء الحساب</button>
            <div id="signup-msg" class="auth-msg" role="status"></div>
          </form>
        </div>
      </div>
      <p class="center mt-3" style="color:var(--ink-faint);font-size:14px">الحسابات مجانية — والحجز ما زال عبر واتساب حالياً.</p>
    </div>

    <div id="member-view" style="display:none">
      <div class="center">
        <p id="member-hello" class="sec-lead"></p>
        <p class="mt-1">
          <a id="admin-link" class="btn btn-primary btn-sm" href="/admin/" style="display:none">لوحة إدارة الاستوديو</a>
          <button id="btn-signout" class="btn btn-ghost btn-sm" type="button">تسجيل الخروج</button>
        </p>
      </div>
      <div class="two-col mt-3">
        <div>
          <h3>هذا الأسبوع في الشالا</h3>
          <div class="schedule-wrap mt-1">
            <table class="schedule">
              <thead><tr><th scope="col">اليوم</th><th scope="col">الحصة</th><th scope="col">الوقت</th></tr></thead>
              <tbody data-live-schedule><tr><td colspan="3">جارٍ تحميل الجدول…</td></tr></tbody>
            </table>
          </div>
          <p class="mt-2"><a class="btn btn-primary btn-sm" data-wa="classes" data-book href="#">احجزي عبر واتساب</a></p>
        </div>
        <div>
          <h3>الأخبار والفعاليات</h3>
          <ul id="member-events" class="member-list mt-1"></ul>
        </div>
      </div>
    </div>
  </div>
</section>
'''

PAGES["account/"] = {
    "title": "حساب الأعضاء — لا ميدوزا · شالا الطيران",
    "desc": "سجّلي الدخول إلى لا ميدوزا لرؤية جدول الحصص المباشر وإعلانات الأعضاء ومواعيد الريتريت أولاً.",
    "body": ACCOUNT_BODY_AR,
    "extra_scripts": '<script src="/assets/js/account.js" defer></script>',
}

BOOK_BODY_AR = '''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">احجزي حصة</span>
    <h1>احجزي <span class="line-accent">أرجوحتك</span></h1>
    <p class="ph-lead">اختاري حصة من الأسبوعين القادمين — مقعدك يُحفظ فور الحجز. الحجز مجاني، والدفع في الاستوديو.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <p id="book-gate" class="note-soft">جارٍ التحقق من حسابك…</p>
    <div id="book-view" style="display:none">
      <div id="book-success"></div>
      <div class="two-col">
        <div>
          <h3>الحصص القادمة</h3>
          <div id="book-days" class="mt-1"></div>
        </div>
        <div>
          <h3>حجوزاتك القادمة</h3>
          <div id="my-bookings" class="mt-1"></div>
          <div class="note-soft mt-2">تغيّرت خططك؟ ألغي الحجز هنا ليأخذ مقعدك شخص آخر. للأسئلة — <a data-wa="classes" href="#">راسلينا على واتساب</a>.</div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

PAGES["book/"] = {
    "title": "احجزي حصة — لا ميدوزا · شالا الطيران، دهب",
    "desc": "احجزي حصتك في اليوغا الهوائية في لا ميدوزا، دهب — جدول مباشر، أماكن متاحة لحظياً، الحجز مجاني والدفع في الاستوديو.",
    "body": BOOK_BODY_AR,
    "extra_scripts": '<script src="/assets/js/booking.js" defer></script>',
}

INQUIRE_BODY_AR = '''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">الاستفسارات</span>
    <h1>أخبرينا بما <span class="line-accent">تخططين له</span></h1>
    <p class="ph-lead">ريتريتات، فعاليات شركات، طلبات أراجيح بالجملة — اكتبيها هنا وسنرد خلال يومي عمل. تفضلين الدردشة؟ <a data-wa="partner" href="#">واتساب يعمل أيضاً</a>.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="auth-card" style="max-width:640px;margin:0 auto">
      <form id="form-inquire">
        <div class="field"><label for="inq-topic">ما موضوع رسالتك؟</label>
          <select id="inq-topic" required>
            <option value="retreat">الريتريتات — مواعيد وحجوزات جماعية</option>
            <option value="corporate">الشركات والشراكات</option>
            <option value="hammocks">الأراجيح — جملة / طلبات مخصصة</option>
            <option value="general">شيء آخر</option>
          </select>
        </div>
        <div class="field"><label for="inq-name">اسمك</label><input id="inq-name" type="text" autocomplete="name" required maxlength="120"></div>
        <div class="field"><label for="inq-contact">البريد الإلكتروني أو رقم واتساب</label><input id="inq-contact" type="text" autocomplete="email" required maxlength="200"></div>
        <div class="field"><label for="inq-message">رسالتك</label><textarea id="inq-message" rows="6" required maxlength="2000"></textarea></div>
        <button id="inq-submit" class="btn btn-primary btn-block" type="submit">أرسلي الاستفسار</button>
        <div id="inq-msg-status" class="auth-msg" role="status"></div>
      </form>
    </div>
  </div>
</section>
'''

PAGES["inquire/"] = {
    "title": "استفسارات الريتريت والشركات والجملة — لا ميدوزا دهب",
    "desc": "أرسلي إلى لا ميدوزا استفساراً مكتوباً عن الريتريتات وفعاليات الشركات والشراكات أو أراجيح الجملة اليدوية. نرد خلال يومي عمل.",
    "body": INQUIRE_BODY_AR,
    "extra_scripts": '<script src="/assets/js/inquire.js" defer></script>',
}
