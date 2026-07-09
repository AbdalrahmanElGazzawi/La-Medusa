# English page bodies + metadata
from common import ART_JELLY, ART_SILK, ICON_WA, art_horizon, cocoon, DOMAIN

CLASSES = [
    ("Aerial flow", "Breath-led vinyasa in and out of the hammock — float, fold and finish upside-down.", "500–650", "All levels", "sea"),
    ("Intro to silks", "Your first flight. Learn the fabric, build trust, leave swaying in a cocoon.", "500", "Beginners", "lav"),
    ("Restorative aerial", "Slow, supported shapes. The hammock holds you so your nervous system can let go.", "500–650", "All levels", "sea"),
    ("Hammock mobility", "Deep hips, spine and shoulder work with the hammock as your mobility tool.", "650", "All levels", "lav"),
    ("Kids & teens aerial", "Play, strength and confidence in the air — safe, supervised, joyful.", "500–650", "Ages 6–15", "sand"),
    ("Therapeutic aerial", "Gentle decompression and targeted release for backs that sit at desks.", "500–650", "All levels", "sea"),
    ("Aerial hoop series", "Artistry and strength on the lyra — a progressive multi-week series.", "500–650", "Progressive", "lav"),
    ("Master silks", "Advanced fabric technique for experienced flyers — wraps, drops-free artistry.", "500–650", "Advanced", "sea"),
    ("Vinyasa & hatha (mat)", "Grounded classes that build the breath and base your aerial practice grows from.", "500–650", "All levels", "sand"),
]

SCHEDULE = [
    ("Sunday", "Aerial Yin", "7:00 PM · all levels"),
    ("Tuesday", "101 Aerials", "7:00 PM · beginner-friendly"),
    ("Thursday", "Aerial Yin", "7:00 PM · all levels"),
    ("Friday", "101 Aerials", "9:00 AM · beginner-friendly"),
]

def class_cards(items):
    out = ""
    for name, desc, price, level, tint in items:
        art = {"sea": "background:var(--seafoam)", "lav": "background:var(--lavender)", "sand": "background:var(--sand-2)"}[tint]
        out += f'''<article class="card reveal">
<div class="card-art" style="{art}"></div>
<h3>{name}</h3>
<p>{desc}</p>
<div class="chip-row"><span class="chip">90 min</span><span class="chip chip-lav">{level}</span></div>
<div class="price-tag">{price} EGP <small>/ session</small></div>
<a class="card-cta" data-wa="classes" data-book href="#">Book this class →</a>
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
    <p class="hero-kicker">Aerial yoga · Assala, Dahab · South Sinai</p>
    <h1>Move beautifully.<br>Feel freely. <span class="line-accent">Fly gracefully.</span></h1>
    <p class="hero-sub">A calm, somatic aerial studio between the Sinai mountains and the Red Sea. Classes begin with gentle stretching, build to inversions, and end swaying in a cocoon.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" data-wa="classes" data-book href="#">{ICON_WA} Book on WhatsApp</a>
      <a class="btn btn-ghost" href="/classes/">Explore classes</a>
    </div>
  </div>
  <div class="horizon">{art_horizon("Illustration of an aerialist suspended in a hammock above the sea and desert of Dahab")}</div>
</section>
<div data-live-news class="container"></div>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="sec-kicker">The shala</span>
        <h2>Where the desert meets the sea — and you meet the air</h2>
        <p class="sec-lead">La Medusa is Dahab's aerial yoga studio. Our practice is soft on purpose: no drops, no tricks-first culture — just breath, fabric, and the slow discovery that your body can hang, fold and fly.</p>
        <p class="sec-lead">Every class ends the same way: wrapped in the hammock, swaying like a jellyfish in still water.</p>
        <a class="btn btn-ghost mt-2" href="/teachers/">Meet your teachers</a>
      </div>
      <div class="photo-slot has-photo reveal" data-photo-slot="home_studio" style="min-height:380px"><img class="photo" src="/assets/img/photos/studio-aerialist.jpg" style="object-position:center 30%" alt="An aerialist stretched in a full pose beneath the painted La Medusa logo in the shala" loading="lazy"></div>
    </div>
  </div>
</section>

{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">Classes</span>
      <h2>Tailored classes for all levels — adults &amp; kids</h2>
      <p class="sec-lead">90-minute sessions from 500–650 EGP. Small groups, one teacher's eyes on every body.</p>
    </div>
    <div class="card-grid">
      {class_cards(CLASSES[:3])}
    </div>
    <p class="center mt-3"><a class="btn btn-sea" href="/classes/">See all classes &amp; schedule</a></p>
  </div>
</section>

{cocoon("#F1EEF8")}
<section class="section section-tint-lav">
  <div class="container">
    <div class="quote-band reveal">
      <blockquote>“Every body is welcome; modify the pose to the person.”</blockquote>
      <cite>The teaching standard we run every class by</cite>
      <p class="mt-2"><a class="btn btn-ghost" href="/accessibility/">Our accessibility promise — every body flies</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">Teacher training</span>
      <h2>The AYTTC — proven, not promised</h2>
    </div>
    <div class="proof-row reveal">
      <div class="proof"><div class="p-num">2</div><div class="p-label">Cohorts delivered — April 2025 &amp; April 2026</div></div>
      <div class="proof"><div class="p-num">Jul '26</div><div class="p-label">Next cohort — enrolling now</div></div>
      <div class="proof"><div class="p-num">E-RYT 200</div><div class="p-label">Led by Mona Shafei, YACEP</div></div>
      <div class="proof"><div class="p-num">Sinai</div><div class="p-label">The peninsula's dedicated aerial yoga teacher training</div></div>
    </div>
    <p class="center mt-3">
      <span class="badge-enrolling">July 2026 cohort — enrolling now</span><br><br>
      <a class="btn btn-primary" href="/teacher-training/">Explore the training</a>
    </p>
  </div>
</section>

{cocoon("#F6F0E3")}
<section class="section section-tint-sand">
  <div class="container">
    <div class="split">
      <div class="photo-slot has-photo reveal" data-photo-slot="retreat_home" style="min-height:340px"><img class="photo" src="/assets/img/photos/pergola-hammocks.jpg" alt="Colorful aerial hammocks hanging in the open-air shala" loading="lazy"></div>
      <div class="reveal">
        <span class="sec-kicker">Retreats</span>
        <h2>Fly where the mountains fall into the sea</h2>
        <p class="sec-lead">Our first retreat ran in 2025. Days of aerial practice, breath and salt water — hosted with licensed partner hotels on Dahab's shore.</p>
        <a class="btn btn-ghost mt-2" href="/retreats/">Retreats &amp; next dates</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="card reveal" style="padding:36px">
        <div class="card-art" style="background:var(--lavender)"></div>
        <h3>Hammocks by Mona Shafei</h3>
        <p>Handcrafted aerial hammocks, tailored to your every move — personalized design, custom colors, made in Dahab. For flyers, studios and hotels.</p>
        <a class="card-cta" href="/hammocks/">The hammock atelier →</a>
      </div>
      <div class="card reveal" style="padding:36px">
        <div class="card-art" style="background:var(--seafoam)"></div>
        <h3>Two founders, one shala</h3>
        <p>Mona Shafei (E-RYT 200, YACEP) leads training, retreats and the hammock atelier. Reem Abuel Ela (YA-certified) makes first flights feel safe, patient and warm.</p>
        <a class="card-cta" href="/teachers/">Meet Mona &amp; Reem →</a>
      </div>
    </div>
  </div>
</section>


{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">Life at the shala</span>
      <h2>Real classes, real people, real flying</h2>
      <p class="sec-lead">Every photo below was taken in our open-air studio in Assala.</p>
    </div>
    <div class="gallery-grid reveal">
      <img class="g-wide" src="/assets/img/photos/group-shala.jpg" alt="A joyful group poses in front of the painted La Medusa logo after class" loading="lazy">
      <img src="/assets/img/photos/community-circle.jpg" alt="The shala community gathered in a circle beneath the silks" loading="lazy">
      <img src="/assets/img/photos/assisted-group.jpg" alt="Students helping each other during a group aerial exercise" loading="lazy">
      <img src="/assets/img/photos/inversion.jpg" alt="A student hangs upside down in an aerial hammock" loading="lazy">
      <img src="/assets/img/photos/partner-practice.jpg" alt="Two students practicing a partner aerial pose" loading="lazy">
    </div>
    <p class="center mt-3"><a class="btn btn-ghost" href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">More on Instagram — @theaerialistshala</a></p>
  </div>
</section>

<section class="section">
  <div class="container center">
    <div class="sec-head center reveal">
      <span class="sec-kicker">Watch</span>
      <h2>The shala in motion</h2>
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
    <h2>Fly with us this week</h2>
    <p class="sec-lead" style="max-width:560px;margin-left:auto;margin-right:auto">Message us on WhatsApp — or DM <strong>“AERIAL”</strong> to <a href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">@theaerialistshala</a> — and we'll find you a hammock.</p>
    <div class="hero-ctas mt-2">
      <a class="btn btn-primary" data-wa="classes" href="#">{ICON_WA} WhatsApp +20 115 616 6225</a>
      <a class="btn btn-ghost" href="/contact/">All ways to reach us</a>
    </div>
  </div>
</section>
'''

CLASSES_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Classes &amp; schedule</span>
    <h1>Tailored classes for <span class="line-accent">every body</span></h1>
    <p class="ph-lead">90-minute sessions in a calm, small-group setting. Pre-booking is required — message us and we'll hold your hammock.</p>
    <div class="hero-ctas"><a class="btn btn-primary" data-wa="classes" data-book href="#">{ICON_WA} Book a class</a></div>
  </div>
  <div class="page-hero-band horizon">{art_horizon("Aerialist above the Dahab shoreline")}</div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head reveal">
      <span class="sec-kicker">The menu</span>
      <h2>Nine ways to fly</h2>
      <p class="sec-lead">All aerial classes include full safety briefing, padded landing zones and a teacher-checked rig. Sessions run 500–650 EGP per person (90 minutes); the exact price of each class is confirmed when you book.</p>
    </div>
    <div class="card-grid">{class_cards(CLASSES)}</div>
    <div class="note-soft mt-3">Schedule and prices are confirmed when you book — dual local / visitor rates and class passes are announced on WhatsApp. Sliding-scale places are available in every class: see our <a href="/accessibility/">accessibility promise</a>.</div>
  </div>
</section>

{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">This week</span>
      <h2>The weekly schedule</h2>
      <p class="sec-lead" data-schedule-status>The studio updates this schedule directly — changes are announced on WhatsApp and Instagram stories too.</p>
    </div>
    <div class="schedule-wrap reveal">
      <table class="schedule">
        <caption class="visually-hidden">Weekly class schedule</caption>
        <thead><tr><th scope="col">Day</th><th scope="col">Class</th><th scope="col">Time &amp; level</th></tr></thead>
        <tbody data-live-schedule>
          {"".join(f'<tr><th scope="row" class="cls">{d}</th><td class="cls">{c}</td><td><span class="meta">{m}</span></td></tr>' for d, c, m in SCHEDULE)}
        </tbody>
      </table>
    </div>
    <p class="center mt-3"><a class="btn btn-primary" data-wa="classes" data-book href="#">{ICON_WA} Get this week's schedule</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <h3>Your first class</h3>
        <ul class="checklist mt-1">
          <li>Come 15 minutes early for your welcome + health intake.</li>
          <li>Wear leggings and a top that covers the underarms — fabric burns are real.</li>
          <li>No rings, watches, zips or oils; hair tied.</li>
          <li>Eat light — nothing heavy for 2 hours before inverting.</li>
          <li>You control every descent. Nothing is forced, ever.</li>
        </ul>
      </div>
      <div class="reveal">
        <h3>Kids fly too</h3>
        <p class="sec-lead">Kids &amp; teens sessions build strength, focus and fearless joy — with the same safety standards as every adult class.</p>
        <a class="btn btn-ghost mt-2" data-wa="kids" href="#">Ask about kids' classes</a>
      </div>
    </div>
  </div>
</section>
'''

AYTTC_JSONLD = f'''<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Aerial Yoga Teacher Training Course (AYTTC) — La Medusa, Dahab",
  "description": "Aerial yoga teacher training in Dahab, Egypt. Led by Mona Shafei (E-RYT 200, YACEP). Cohorts delivered April 2025 and April 2026; July 2026 cohort enrolling now.",
  "provider": {{ "@type": "Organization", "name": "La Medusa · The Aerialist Shala", "sameAs": "https://www.instagram.com/theaerialistshala/" }},
  "hasCourseInstance": {{
    "@type": "CourseInstance",
    "courseMode": "onsite",
    "location": {{ "@type": "Place", "name": "La Medusa · The Aerialist Shala", "address": {{ "@type": "PostalAddress", "addressLocality": "Dahab", "addressRegion": "South Sinai", "addressCountry": "EG" }} }},
    "startDate": "2026-07"
  }}
}}</script>'''

AYTTC_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="badge-enrolling">July 2026 cohort — enrolling now</span>
    <h1 class="mt-2">Become an aerial yoga teacher — <span class="line-accent">in Dahab</span></h1>
    <p class="ph-lead">The AYTTC is Sinai's dedicated aerial yoga teacher training: small cohorts, real teaching practice, and a curriculum built from our own Pose &amp; Practice Manual.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" data-wa="ayttc" href="#">{ICON_WA} Reserve your spot</a>
      <a class="btn btn-ghost" href="#curriculum">See the curriculum</a>
    </div>
  </div>
  <div class="page-hero-band horizon">{art_horizon("Aerialist training over the Dahab horizon")}</div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">Track record</span>
      <h2>Proven, not promised</h2>
    </div>
    <div class="proof-row reveal">
      <div class="proof"><div class="p-num">Apr '25</div><div class="p-label">First cohort delivered</div></div>
      <div class="proof"><div class="p-num">Apr '26</div><div class="p-label">Second cohort delivered</div></div>
      <div class="proof"><div class="p-num">Jul '26</div><div class="p-label">Third cohort — enrolling</div></div>
      <div class="proof"><div class="p-num">Small</div><div class="p-label">Cohorts kept small — everyone teaches, everyone is seen</div></div>
    </div>
    <div class="two-col mt-3">
      <div class="photo-slot has-photo reveal" data-photo-slot="ayttc_2025"><img class="photo" src="/assets/img/photos/practice-assist.jpg" alt="A teacher giving a hands-on adjustment during aerial practice" loading="lazy"></div>
      <div class="photo-slot has-photo reveal" data-photo-slot="ayttc_2026"><img class="photo" src="/assets/img/photos/teaching-spot.jpg" alt="Students watch as a teacher spots an inversion in the studio" loading="lazy"></div>
    </div>
  </div>
</section>

{cocoon("#F1EEF8")}
<section class="section section-tint-lav" id="curriculum">
  <div class="container">
    <div class="sec-head reveal">
      <span class="sec-kicker">Curriculum</span>
      <h2>What you'll learn</h2>
      <p class="sec-lead">Built from the La Medusa Pose &amp; Practice Manual and led by Mona Shafei (E-RYT 200, YACEP) — training that counts toward Yoga Alliance continuing education.</p>
    </div>
    <ul class="timeline reveal">
      <li><span class="tl-when">Module 1</span><h3>Foundations of flight</h3><p>Aerial hammock lineage, the La Medusa method, and the somatic principles behind a practice that calms as it strengthens.</p></li>
      <li><span class="tl-when">Module 2</span><h3>Rigging &amp; safety</h3><p>Engineering safety factors, hardware standards, daily and monthly inspection routines — the non-negotiables that make you insurable and trustworthy.</p></li>
      <li><span class="tl-when">Module 3</span><h3>Asana in the air</h3><p>The full pose library: entries, exits, spotting, contraindications, and the defining rule — the student always controls the descent.</p></li>
      <li><span class="tl-when">Module 4</span><h3>Every-body teaching</h3><p>Modify the pose to the person: adaptations for body types, abilities, injuries and fears. This is core curriculum here, not a footnote.</p></li>
      <li><span class="tl-when">Module 5</span><h3>Sequencing &amp; the cocoon</h3><p>Design 90-minute journeys that open gently, peak safely and land everyone in stillness.</p></li>
      <li><span class="tl-when">Module 6</span><h3>Teaching practicum</h3><p>Real students, real feedback, every day — you graduate having actually taught.</p></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <h3>Who it's for</h3>
        <ul class="checklist mt-1">
          <li>Yoga teachers adding a certified aerial specialty.</li>
          <li>Dedicated practitioners ready to teach their first class.</li>
          <li>Movement professionals — dancers, physios, freedive coaches.</li>
          <li>No handstand required. Consistent practice is.</li>
        </ul>
      </div>
      <div class="reveal">
        <h3>Enrolment — July 2026</h3>
        <p class="sec-lead">Places are limited to keep cohorts small. A deposit holds your spot; tuition, payment plans and the full information pack come by WhatsApp.</p>
        <a class="btn btn-primary mt-2" data-wa="ayttc" href="#">{ICON_WA} Request the info pack</a>
      </div>
    </div>
    <div class="note-soft mt-3">Graduates leave with the Pose &amp; Practice Manual, a teaching certificate from La Medusa, and continuing-education hours with our YACEP lead teacher. Ask us how the training fits your Yoga Alliance profile.</div>
  </div>
</section>
'''

RETREATS_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Retreats</span>
    <h1>Days of air, breath and <span class="line-accent">salt water</span></h1>
    <p class="ph-lead">Aerial yoga retreats where the Sinai desert falls into the Red Sea — morning flights, freediving-friendly afternoons, cocoon sunsets.</p>
    <div class="hero-ctas"><a class="btn btn-primary" data-wa="retreat" href="#">{ICON_WA} Join the retreat list</a></div>
  </div>
  <div class="page-hero-band horizon">{art_horizon("Retreat scene: aerialist above the sea at sunset")}</div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="sec-kicker">2025 — delivered</span>
        <h2>Our first retreat — delivered</h2>
        <p class="sec-lead">A week of aerial practice, mobility, Dahab's slow mornings and long sea afternoons. The next edition builds on everything we learned.</p>
        <p class="sec-lead">Accommodation is hosted with licensed partner hotels on the Dahab shore — you sleep legally, comfortably and steps from the water.</p>
      </div>
      <div class="photo-slot has-photo reveal" data-photo-slot="retreat_2025" style="min-height:360px"><img class="photo" src="/assets/img/photos/restorative.jpg" alt="Students resting in a supported restorative aerial pose" loading="lazy"></div>
    </div>
  </div>
</section>

{cocoon("#F6F0E3")}
<section class="section section-tint-sand">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="sec-kicker">What a retreat day looks like</span>
      <h2>The rhythm</h2>
    </div>
    <div class="card-grid reveal">
      <article class="card"><div class="card-art" style="background:var(--seafoam)"></div><h3>Morning</h3><p>Sunrise breath work and a full aerial practice before the heat — the desert light does half the teaching.</p></article>
      <article class="card"><div class="card-art" style="background:var(--lavender)"></div><h3>Afternoon</h3><p>Free time in the freediving capital of the world: reef, blue hole trips, café hours, massage, nothing at all.</p></article>
      <article class="card"><div class="card-art" style="background:var(--sand-2)"></div><h3>Sunset</h3><p>Restorative aerial and the cocoon as the mountains turn violet. Dinner together under the stars.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="two-col">
      <div class="reveal">
        <h3>Next dates</h3>
        <p class="sec-lead">The next retreat is planned for the high-season window (October–April). Dates, international pricing in USD/EUR, and early-bird places are announced to the WhatsApp list first.</p>
        <a class="btn btn-primary mt-2" data-wa="retreat" href="#">{ICON_WA} Get dates &amp; pricing first</a>
        <p class="mt-1" style="font-size:14px"><a href="/inquire/?topic=retreat">Prefer email? Send a retreat inquiry →</a></p>
      </div>
      <div class="reveal">
        <h3>Good to know</h3>
        <ul class="checklist mt-1">
          <li>All levels welcome — including first-time flyers.</li>
          <li>Licensed hotel partners handle accommodation.</li>
          <li>Small groups by design.</li>
          <li>Solo travellers are warmly welcome.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''

TEACHERS_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Teachers</span>
    <h1>Two founders, <span class="line-accent">one shala</span></h1>
    <p class="ph-lead">La Medusa is founded, taught and hand-sewn by two women who believe the air belongs to every body.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="teacher-grid">
      <article class="teacher reveal">
        <div class="photo-slot" role="img" aria-label="Photo slot: portrait of Mona Shafei" data-photo-slot="teacher_mona">{ART_SILK}<span class="ps-label">Photo slot — Mona Shafei</span></div>
        <div class="teacher-body">
          <h3>Mona Shafei</h3>
          <p class="t-creds">E-RYT 200 · YACEP · Founder</p>
          <p>Head of training &amp; product. Mona leads the AYTTC teacher training (cohorts delivered April 2025 and April 2026), designs the retreats, teaches hammock mobility — and makes the hammocks themselves under <a href="/hammocks/">Hammocks by Mona Shafei</a>. Her wider practice spans Chi Nei Tsang bodywork.</p>
          <p class="mt-1"><a href="https://www.instagram.com/yogawith_mona/" target="_blank" rel="noopener">@yogawith_mona</a></p>
        </div>
      </article>
      <article class="teacher reveal">
        <div class="photo-slot" role="img" aria-label="Photo slot: portrait of Reem Abuel Ela" data-photo-slot="teacher_reem">{ART_SILK}<span class="ps-label">Photo slot — Reem Abuel Ela</span></div>
        <div class="teacher-body">
          <h3>Reem Abuel Ela</h3>
          <p class="t-creds">YA-certified aerial teacher · Co-founder</p>
          <p>Head of studio &amp; community. Reem teaches aerial yoga and silks with the warm, patient guidance that makes first-timers feel held — literally. She is the shala's bilingual voice, its artist, and the reason the community feels like one.</p>
          <p class="mt-1"><a href="https://www.instagram.com/profoundlytrue/" target="_blank" rel="noopener">@profoundlytrue</a></p>
        </div>
      </article>
    </div>
  </div>
</section>


<section class="section">
  <div class="container">
    <div class="photo-slot has-photo reveal" style="min-height:420px"><img class="photo" src="/assets/img/photos/group-shala.jpg" alt="Teachers and students together in front of the La Medusa wall" loading="lazy"></div>
  </div>
</section>
{cocoon("#F1EEF8")}
<section class="section section-tint-lav">
  <div class="container">
    <div class="quote-band reveal">
      <blockquote>“Calm on purpose: begin with gentle stretching, build to inversions, end in a swaying cocoon.”</blockquote>
      <cite>The La Medusa method</cite>
      <p class="mt-2"><a class="btn btn-primary" data-wa="classes" href="#">{ICON_WA} Take a class with us</a></p>
    </div>
  </div>
</section>
'''

HAMMOCKS_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Hammocks by Mona Shafei</span>
    <h1>Handcrafted hammocks, tailored to <span class="line-accent">your every move</span></h1>
    <p class="ph-lead">Every La Medusa hammock is cut and sewn by Mona in Dahab — woven with 70% natural cotton, personalized design, custom colors, made for real practice.</p>
    <div class="hero-ctas"><a class="btn btn-primary" data-wa="hammocks" href="#">{ICON_WA} Ask for the catalog</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="card-grid">
      <article class="card reveal"><div class="card-art" style="background:var(--seafoam)"></div><h3>For your practice</h3><p>A hammock in your colors, sized to your height and ceiling — with honest guidance on rigging it safely at home.</p><a class="card-cta" data-wa="hammocks" href="#">Order yours →</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--lavender)"></div><h3>For studios &amp; hotels</h3><p>Wholesale sets for studios, retreat venues and hotels across Egypt and MENA — rigging guidance included with every order.</p><a class="card-cta" data-wa="partner" href="#">Wholesale enquiry →</a><br><a class="card-cta" href="/inquire/?topic=hammocks">Or send a written inquiry →</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--sand-2)"></div><h3>Made to be trusted</h3><p>The same fabric and rated hardware standards we hang our own students from — because we do, every day, in the shala.</p><a class="card-cta" href="/accessibility/">Our safety standards →</a></article>
    </div>
    <div class="two-col mt-3">
      <div class="photo-slot has-photo reveal" data-photo-slot="hammocks_fabric"><img class="photo" src="/assets/img/photos/fabric-yellow.jpg" alt="Yellow handmade aerial hammocks hanging against a blue wall" loading="lazy"></div>
      <div class="photo-slot has-photo reveal" data-photo-slot="hammocks_atelier"><img class="photo" src="/assets/img/photos/brand-tote.jpg" alt="A Hammocks by Mona Shafei tote bag" loading="lazy"></div>
    </div>
    <div class="note-soft mt-3">Pricing and current color runs live in the WhatsApp catalog — message <strong>“HAMMOCKS”</strong> and Mona will send it over. Follow <a href="https://www.instagram.com/hammocksbymonashafei/" target="_blank" rel="noopener">@hammocksbymonashafei</a> for new collections.</div>
  </div>
</section>
'''

ACCESS_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">The promise</span>
    <h1>Every body <span class="line-accent">flies</span></h1>
    <p class="ph-lead">“Every body is welcome; modify the pose to the person” isn't a slogan we added — it's the teaching standard the shala was built on. Here is what it means in practice, published so you can hold us to it.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <ul class="timeline reveal">
      <li class="tl-done"><span class="tl-when">Live now</span><h3>The every-body teaching standard</h3><p>Adaptations for body type, ability, injury and fear are core curriculum in every class and in our teacher training — never an afterthought.</p></li>
      <li class="tl-done"><span class="tl-when">Live now</span><h3>Bilingual everything</h3><p>Arabic and English waivers, signage, guides and classes. Half our community is local; respect is retention.</p></li>
      <li class="tl-now"><span class="tl-when">Q4 2026</span><h3>Sliding-scale pricing</h3><p>Three self-selected tiers — community-supporter, standard, supported — no proof of need asked, ever. Locals stay in the room in a tourist economy.</p></li>
      <li class="tl-now"><span class="tl-when">Q4 2026</span><h3>Prenatal &amp; recovery pathway</h3><p>Group aerial classes are contraindicated in pregnancy, so we offer private, medically-cleared prenatal-adapted work — and a post-injury track with your GP's letter.</p></li>
      <li><span class="tl-when">Q1 2027</span><h3>Access audit &amp; low-sensory slot</h3><p>Entrance, bathroom and mounting-aid audit; low-hammock formats for limited mobility; one quiet, low-sensory class slot each week.</p></li>
      <li><span class="tl-when">2027</span><h3>Adaptive aerial</h3><p>A wheelchair-user aerial program modelled on proven adaptive programs abroad — silks for spinal decompression, trained-assistant protocols, one monthly session to start. We aim to make it a first for Egypt.</p></li>
    </ul>
  </div>
</section>

{cocoon("#EAF6F4")}
<section class="section section-tint-sea">
  <div class="container">
    <div class="sec-head reveal">
      <span class="sec-kicker">Safety is the brand</span>
      <h2>The non-negotiables</h2>
      <p class="sec-lead">Aerial yoga is safe the way flying is safe: because of systems, not luck.</p>
    </div>
    <div class="card-grid reveal">
      <article class="card"><div class="card-art" style="background:var(--seafoam)"></div><h3>Engineered rigging</h3><p>5:1 to 10:1 safety factors, two independent engineer-verified anchors per point (≥500 kg each), climbing-rated hardware only.</p></article>
      <article class="card"><div class="card-art" style="background:var(--lavender)"></div><h3>Checked daily</h3><p>Teacher load-tests every hammock every day; documented monthly inspections; fabric and hardware retired at the first sign of wear.</p></article>
      <article class="card"><div class="card-art" style="background:var(--sand-2)"></div><h3>The defining rule</h3><p>No inversion higher than standing. No drops, no swinging into load. The student always controls the descent.</p></article>
      <article class="card"><div class="card-art" style="background:var(--seafoam)"></div><h3>Screened before flight</h3><p>A health intake for every new student — pregnancy, blood pressure, glaucoma, recent surgery, vertigo — and honest answers about when not to invert.</p></article>
      <article class="card"><div class="card-art" style="background:var(--lavender)"></div><h3>Ready for anything</h3><p>First Aid &amp; CPR current for all teachers, padded landing zones under every hammock, clear emergency protocols.</p></article>
      <article class="card"><div class="card-art" style="background:var(--sand-2)"></div><h3>If anything is uncertain</h3><p>…the class does not fly. It's that simple.</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container center reveal">
    <h2>Not sure aerial is for you?</h2>
    <p class="sec-lead" style="max-width:560px;margin:16px auto 0">That's exactly who this page is for. Tell us about your body, and we'll tell you honestly what your first class can look like.</p>
    <div class="hero-ctas mt-2"><a class="btn btn-primary" data-wa="access" href="#">{ICON_WA} Ask us anything</a></div>
  </div>
</section>
'''

CONTACT_BODY = f'''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Contact</span>
    <h1>Find us where the mountains <span class="line-accent">meet the sea</span></h1>
    <p class="ph-lead">Everything runs through WhatsApp — booking, questions, teacher training, hammock orders. One number, real humans.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="card-grid">
      <article class="card reveal"><div class="card-art" style="background:var(--seafoam)"></div><h3>Book a class</h3><p>Message us and we'll send this week's schedule and hold your hammock.</p><a class="btn btn-primary" data-wa="classes" href="#">{ICON_WA} Book a class</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--lavender)"></div><h3>Teacher training</h3><p>July 2026 cohort enrolling — get the info pack and deposit details.</p><a class="btn btn-primary" data-wa="ayttc" href="#">{ICON_WA} AYTTC info pack</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--sand-2)"></div><h3>Retreats</h3><p>Join the list that hears dates and early-bird pricing first.</p><a class="btn btn-primary" data-wa="retreat" href="#">{ICON_WA} Retreat list</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--seafoam)"></div><h3>Hammocks</h3><p>Order a custom hammock or ask about wholesale for your studio or hotel.</p><a class="btn btn-primary" data-wa="hammocks" href="#">{ICON_WA} Hammock catalog</a></article>
      <article class="card reveal"><div class="card-art" style="background:var(--lavender)"></div><h3>Partnerships &amp; events</h3><p>Corporate offsites, festivals, venue classes, brand collaborations.</p><a class="btn btn-primary" data-wa="partner" href="#">{ICON_WA} Partner with us</a><p class="mt-1" style="font-size:13.5px"><a href="/inquire/?topic=corporate">Or send a written inquiry →</a></p></article>
      <article class="card reveal"><div class="card-art" style="background:var(--sand-2)"></div><h3>Prefer Instagram?</h3><p>DM the word <strong>“AERIAL”</strong> to @theaerialistshala and we'll take it from there.</p><a class="btn btn-ghost" href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">Open Instagram</a></article>
    </div>

    <div class="two-col mt-3">
      <div class="reveal">
        <h3>The studio</h3>
        <p class="sec-lead">La Medusa · The Aerialist Shala<br>Assala, Dahab, South Sinai, Egypt</p>
        <p class="sec-lead">WhatsApp: <a data-wa="general" href="#">+20 115 616 6225</a><br>
        Instagram: <a href="https://www.instagram.com/theaerialistshala/" target="_blank" rel="noopener">@theaerialistshala</a></p>
        <p class="sec-lead"><a href="https://maps.google.com/?q=Assala,+Dahab,+South+Sinai,+Egypt" target="_blank" rel="noopener">Open in Google Maps →</a></p>
      </div>
      <div class="reveal">
        <h3>Before you arrive</h3>
        <ul class="checklist mt-1">
          <li>Pre-booking is required — we keep groups small.</li>
          <li>New students arrive 15 minutes early for the health intake.</li>
          <li>The live weekly schedule is posted on WhatsApp &amp; IG stories.</li>
          <li>Arabic or English — whichever feels like home.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''

HOME_JSONLD = f'''<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "La Medusa · The Aerialist Shala",
  "description": "Aerial yoga studio in Assala, Dahab, Egypt. Classes for all levels (adults & kids), aerial yoga teacher training (AYTTC), retreats and handmade aerial hammocks.",
  "url": "{DOMAIN}/",
  "telephone": "+201156166225",
  "image": "{DOMAIN}/assets/img/logo.png",
  "address": {{ "@type": "PostalAddress", "addressLocality": "Dahab", "addressRegion": "South Sinai", "addressCountry": "EG", "streetAddress": "Assala" }},
  "geo": {{ "@type": "GeoCoordinates", "latitude": 28.509, "longitude": 34.513 }},
  "sameAs": [
    "https://www.instagram.com/theaerialistshala/",
    "https://www.instagram.com/yogawith_mona/",
    "https://www.instagram.com/profoundlytrue/",
    "https://www.instagram.com/hammocksbymonashafei/"
  ],
  "priceRange": "EGP 500–650",
  "slogan": "Move beautifully. Feel freely. Fly gracefully."
}}</script>'''

PAGES = {
    "": {
        "title": "La Medusa · The Aerialist Shala — Aerial Yoga in Dahab, Egypt",
        "desc": "Aerial yoga in Dahab: classes for all levels (adults & kids), aerial yoga teacher training in Egypt, Red Sea retreats and handmade hammocks. Book on WhatsApp.",
        "body": HOME_BODY,
        "jsonld": HOME_JSONLD,
    },
    "classes/": {
        "title": "Aerial Yoga Classes & Schedule in Dahab — La Medusa",
        "desc": "Aerial yoga classes in Dahab from 500–650 EGP: aerial flow, silks, restorative, kids & teens, hoop and more. 90-minute small-group sessions. Book via WhatsApp.",
        "body": CLASSES_BODY,
    },
    "teacher-training/": {
        "title": "Aerial Yoga Teacher Training in Egypt — AYTTC July 2026 | La Medusa Dahab",
        "desc": "The AYTTC aerial yoga teacher training in Dahab, Egypt. Cohorts delivered April 2025 & 2026 — July 2026 enrolling now. Led by Mona Shafei, E-RYT 200 YACEP.",
        "body": AYTTC_BODY,
        "jsonld": AYTTC_JSONLD,
    },
    "retreats/": {
        "title": "Aerial Yoga Retreats in Dahab, Egypt — La Medusa",
        "desc": "Aerial yoga retreats on the Red Sea: morning flights, desert-meets-sea sunsets, licensed partner hotels. 2025 retreat delivered — join the list for next dates.",
        "body": RETREATS_BODY,
    },
    "teachers/": {
        "title": "Our Teachers — Mona Shafei & Reem Abuel Ela | La Medusa Dahab",
        "desc": "Meet the founders of La Medusa: Mona Shafei (E-RYT 200, YACEP, AYTTC lead) and Reem Abuel Ela (YA-certified aerial & silks teacher).",
        "body": TEACHERS_BODY,
    },
    "hammocks/": {
        "title": "Hammocks by Mona Shafei — Handmade Aerial Hammocks, Dahab",
        "desc": "Handcrafted aerial yoga hammocks made in Dahab — personalized design, custom colors, wholesale for studios & hotels. Order via WhatsApp catalog.",
        "body": HAMMOCKS_BODY,
    },
    "accessibility/": {
        "title": "Every Body Flies — Our Accessibility Promise | La Medusa Dahab",
        "desc": "Sliding-scale pricing, adaptive aerial, prenatal pathways, bilingual classes and published safety standards. La Medusa's accessibility promise, in writing.",
        "body": ACCESS_BODY,
    },
    "contact/": {
        "title": "Contact & Booking — La Medusa · The Aerialist Shala, Dahab",
        "desc": "Book aerial yoga in Dahab via WhatsApp +20 115 616 6225 or DM 'AERIAL' on Instagram. Classes, teacher training, retreats, hammocks and partnerships.",
        "body": CONTACT_BODY,
    },
}


ACCOUNT_BODY = '''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Members</span>
    <h1>Your <span class="line-accent">shala account</span></h1>
    <p class="ph-lead">Sign in to see the live schedule, member announcements and retreat dates before anyone else.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div id="auth-view">
      <div class="two-col" style="max-width:940px;margin:0 auto">
        <div class="auth-card">
          <h3>Sign in</h3>
          <form id="form-signin" class="mt-1">
            <div class="field"><label for="si-email">Email</label><input id="si-email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="si-pw">Password</label><input id="si-pw" type="password" autocomplete="current-password" required></div>
            <button class="btn btn-primary btn-block" type="submit">Sign in</button>
            <div id="signin-msg" class="auth-msg" role="status"></div>
          </form>
          <p class="auth-alt"><button id="btn-reset" class="btn btn-ghost btn-sm" type="button">Forgot password?</button></p>
        </div>
        <div class="auth-card">
          <h3>New here? Create an account</h3>
          <form id="form-signup" class="mt-1">
            <div class="field"><label for="su-name">Your name</label><input id="su-name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="su-email">Email</label><input id="su-email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="su-pw">Password (min 6 characters)</label><input id="su-pw" type="password" autocomplete="new-password" required></div>
            <button class="btn btn-sea btn-block" type="submit">Create account</button>
            <div id="signup-msg" class="auth-msg" role="status"></div>
          </form>
        </div>
      </div>
      <p class="center mt-3" style="color:var(--ink-faint);font-size:14px">Accounts are free — booking still happens on WhatsApp for now.</p>
    </div>

    <div id="member-view" style="display:none">
      <div class="center">
        <p id="member-hello" class="sec-lead"></p>
        <p class="mt-1">
          <a id="admin-link" class="btn btn-primary btn-sm" href="/admin/" style="display:none">Studio management panel</a>
          <button id="btn-signout" class="btn btn-ghost btn-sm" type="button">Sign out</button>
        </p>
      </div>
      <div class="two-col mt-3">
        <div>
          <h3>This week at the shala</h3>
          <div class="schedule-wrap mt-1">
            <table class="schedule">
              <thead><tr><th scope="col">Day</th><th scope="col">Class</th><th scope="col">Time</th></tr></thead>
              <tbody data-live-schedule><tr><td colspan="3">Loading schedule…</td></tr></tbody>
            </table>
          </div>
          <p class="mt-2"><a class="btn btn-primary btn-sm" data-wa="classes" data-book href="#">Book on WhatsApp</a></p>
        </div>
        <div>
          <h3>News &amp; events</h3>
          <ul id="member-events" class="member-list mt-1"></ul>
        </div>
      </div>
    </div>
  </div>
</section>
'''

PAGES["account/"] = {
    "title": "Member Account — La Medusa · The Aerialist Shala",
    "desc": "Sign in to La Medusa to see the live class schedule, member announcements and retreat dates first.",
    "body": ACCOUNT_BODY,
    "extra_scripts": '<script src="/assets/js/account.js" defer></script>',
}

BOOK_BODY = '''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Book a class</span>
    <h1>Hold your <span class="line-accent">hammock</span></h1>
    <p class="ph-lead">Pick a class from the next two weeks — your seat is held the moment you book. Booking is free; you pay at the studio.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <p id="book-gate" class="note-soft">Checking your account…</p>
    <div id="book-view" style="display:none">
      <div id="book-success"></div>
      <div class="two-col">
        <div>
          <h3>Upcoming classes</h3>
          <div id="book-days" class="mt-1"></div>
        </div>
        <div>
          <h3>Your upcoming bookings</h3>
          <div id="my-bookings" class="mt-1"></div>
          <div class="note-soft mt-2">Plans changed? Cancel here so someone else can take the seat. Questions — <a data-wa="classes" href="#">message us on WhatsApp</a>.</div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

PAGES["book/"] = {
    "title": "Book a Class — La Medusa · The Aerialist Shala, Dahab",
    "desc": "Book your aerial yoga class at La Medusa, Dahab — live schedule, real-time availability, free to book, pay at the studio.",
    "body": BOOK_BODY,
    "extra_scripts": '<script src="/assets/js/booking.js" defer></script>',
}

INQUIRE_BODY = '''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Inquiries</span>
    <h1>Tell us what you're <span class="line-accent">planning</span></h1>
    <p class="ph-lead">Retreats, corporate events, wholesale hammock orders — write it here and we'll reply within two working days. Prefer chat? <a data-wa="partner" href="#">WhatsApp works too</a>.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="auth-card" style="max-width:640px;margin:0 auto">
      <form id="form-inquire">
        <div class="field"><label for="inq-topic">What is this about?</label>
          <select id="inq-topic" required>
            <option value="retreat">Retreats — dates, group bookings</option>
            <option value="corporate">Corporate &amp; partnerships</option>
            <option value="hammocks">Hammocks — wholesale / custom orders</option>
            <option value="general">Something else</option>
          </select>
        </div>
        <div class="field"><label for="inq-name">Your name</label><input id="inq-name" type="text" autocomplete="name" required maxlength="120"></div>
        <div class="field"><label for="inq-contact">Email or WhatsApp number</label><input id="inq-contact" type="text" autocomplete="email" required maxlength="200"></div>
        <div class="field"><label for="inq-message">Your message</label><textarea id="inq-message" rows="6" required maxlength="2000"></textarea></div>
        <button id="inq-submit" class="btn btn-primary btn-block" type="submit">Send inquiry</button>
        <div id="inq-msg-status" class="auth-msg" role="status"></div>
      </form>
    </div>
  </div>
</section>
'''

PAGES["inquire/"] = {
    "title": "Retreat, Corporate & Wholesale Inquiries — La Medusa Dahab",
    "desc": "Send La Medusa a written inquiry about retreats, corporate events and partnerships, or wholesale handmade aerial hammocks. We reply within two working days.",
    "body": INQUIRE_BODY,
    "extra_scripts": '<script src="/assets/js/inquire.js" defer></script>',
}

ADMIN_BODY = '''
<section class="page-hero">
  <div class="container">
    <span class="sec-kicker">Studio management</span>
    <h1>Run the <span class="line-accent">shala</span></h1>
    <p class="ph-lead">Schedule, events, photos and admins — changes go live on the website instantly.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <p id="gate" class="note-soft">Checking your access…</p>
    <div id="panel-wrap" style="display:none">
      <div class="admin-tabs">
        <button class="on" data-p="sched">Schedule</button>
        <button data-p="bookings">Bookings</button>
        <button data-p="inbox">Inbox</button>
        <button data-p="events">Events &amp; news</button>
        <button data-p="photos">Photos</button>
        <button data-p="admins">Admins</button>
      </div>

      <div class="admin-panel on" id="panel-sched">
        <div style="overflow-x:auto">
        <table class="admin-table" style="min-width:900px">
          <thead><tr><th>Day</th><th>Time</th><th>Class (EN)</th><th>Class (AR)</th><th>Level</th><th>EGP</th><th>Seats</th><th>Live</th><th></th></tr></thead>
          <tbody id="sched-body"></tbody>
        </table>
        </div>
        <p class="mt-2"><button id="btn-add-slot" class="btn btn-primary btn-sm" type="button">Add a class slot</button></p>
        <p class="mt-1" style="font-size:13.5px;color:var(--ink-faint)">Untick “Live” to hide a class without deleting it. Price can stay empty. “Seats” is the booking capacity per class.</p>
      </div>

      <div class="admin-panel" id="panel-bookings">
        <div style="overflow-x:auto">
        <table class="admin-table" style="min-width:820px">
          <thead><tr><th>Date</th><th>Class</th><th>Member</th><th>Email</th><th>Seats used</th></tr></thead>
          <tbody id="bookings-body"></tbody>
        </table>
        </div>
        <p class="mt-1" style="font-size:13.5px;color:var(--ink-faint)">Upcoming confirmed bookings. Members booked on the website; payment still happens at the studio.</p>
      </div>

      <div class="admin-panel" id="panel-inbox">
        <div style="overflow-x:auto">
        <table class="admin-table" style="min-width:980px">
          <thead><tr><th>Date</th><th>Topic</th><th>Name</th><th>Contact</th><th>Message</th><th>Status</th></tr></thead>
          <tbody id="inbox-body"></tbody>
        </table>
        </div>
        <p class="mt-1" style="font-size:13.5px;color:var(--ink-faint)">Written inquiries from the /inquire/ page — retreats, corporate, hammocks. Highlighted rows are new. Reply by email or WhatsApp, then mark as replied.</p>
      </div>

      <div class="admin-panel" id="panel-events">
        <div style="overflow-x:auto">
        <table class="admin-table" style="min-width:980px">
          <thead><tr><th>Type</th><th>Title EN / AR</th><th>Text EN / AR</th><th>Date</th><th>Published</th><th>Members only</th><th></th></tr></thead>
          <tbody id="ev-body"></tbody>
        </table>
        </div>
        <p class="mt-2"><button id="btn-add-event" class="btn btn-primary btn-sm" type="button">Add event / announcement</button></p>
        <p class="mt-1" style="font-size:13.5px;color:var(--ink-faint)">The newest published public item also shows as a banner on the home page. “Members only” items appear just in the members area.</p>
      </div>

      <div class="admin-panel" id="panel-photos">
        <div id="photo-list"></div>
        <p class="mt-1" style="font-size:13.5px;color:var(--ink-faint)">Photos replace the placeholder art on the site the moment they upload. Keep files under 4 MB — export from your phone at medium size so pages stay fast on Dahab internet.</p>
      </div>

      <div class="admin-panel" id="panel-admins">
        <table class="admin-table" style="max-width:560px">
          <thead><tr><th>Admin email</th><th></th></tr></thead>
          <tbody id="admin-body"></tbody>
        </table>
        <div class="mt-2" style="display:flex;gap:10px;max-width:560px">
          <input id="new-admin-email" type="email" placeholder="name@email.com" style="flex:1;padding:11px 14px;border:1.5px solid var(--sea-tint-2);border-radius:12px;font-family:var(--font-sans)">
          <button id="btn-add-admin" class="btn btn-sea btn-sm" type="button">Add admin</button>
        </div>
        <p class="mt-1" style="font-size:13.5px;color:var(--ink-faint)">If they already have an account they become admin immediately; otherwise it applies when they sign up with this email.</p>
      </div>
    </div>
  </div>
</section>
'''
