# La Medusa · The Aerialist Shala — Website (Phase 1)

Bilingual (EN/AR) static showcase site for the aerial yoga studio in Assala, Dahab.
Pure HTML/CSS/JS — no build step required to deploy, no dependencies, fast on weak connections.

## Deploy (Vercel + GitHub)

1. Create the repo: https://github.com/new → name `la-medusa-website`, no README.
2. Get the files in — either way works:
   - **With git installed** (from inside this folder):
     ```
     git init -b main
     git add -A
     git commit -m "La Medusa website — Phase 1"
     git remote add origin https://github.com/YOUR-USERNAME/la-medusa-website.git
     git push -u origin main
     ```
   - **Without git**: on your new empty repo page, click "uploading an existing file" and drag the entire contents of this folder (subfolders included) into the upload area, then Commit.
3. Deploy: https://vercel.com/new → Import `la-medusa-website` → Framework preset: **Other** → no build command, output directory: **`.`** → Deploy.

Netlify / GitHub Pages / any static host works identically.

## Structure

```
index.html            English pages (8): home, classes/, teacher-training/,
<page>/index.html     retreats/, teachers/, hammocks/, accessibility/, contact/
ar/...                Arabic mirror of all 8 pages (RTL)
assets/css/main.css   Design system (brand tokens at the top)
assets/js/config.js   ← EDIT THIS ONE: WhatsApp number, analytics IDs, WA messages
assets/js/main.js     Behavior: WA deep links, nav, reveal, analytics loader
assets/img/           logo.png (approved logo), og.png (social share card)
builder/              Python generator (edit content here, run `python3 build.py`)
sitemap.xml, robots.txt, vercel.json
```

## Editing content

Option A (single edits): edit the HTML files directly.
Option B (recommended): edit `builder/pages_en.py` / `builder/pages_ar.py` (all copy lives there)
and run `python3 builder/build.py` — regenerates all 16 pages + sitemap.

## Before launch checklist

- [ ] **Domain**: currently placeholdered as `lamedusadahab.com`. When decided, set `DOMAIN` in `builder/common.py` and rebuild (or find-replace in HTML + sitemap.xml + robots.txt).
- [ ] **Photos**: every dashed box labeled "Photo slot" is sized and waiting for real photography (studio, cohorts, retreat 2025, Mona, Reem, hammock fabrics). Replace by dropping an `<img>` into the `.photo-slot` div — labels say exactly what goes where.
- [ ] **Arabic review**: all AR copy is a working draft — have Reem review before launch.
- [ ] **Prices**: 500 (Intro silks) and 650 EGP (Hammock mobility) are verified; the other class prices are placed within the 500–650 menu range — confirm each with Mona/Reem.
- [ ] **Schedule**: the weekly grid is a sample; align with the real weekly posting.
- [ ] **Analytics**: paste GA4 + Meta Pixel IDs into `assets/js/config.js` (scripts load only when set). WhatsApp clicks are pre-wired as `whatsapp_click` events with CTA context.
- [ ] **Curriculum wording**: AYTTC modules were drafted to match the Pose & Practice Manual's spirit — verify module names against the actual manual, and confirm the Yoga Alliance positioning language with Mona.

## Phase 2 — LIVE: accounts, live schedule, studio management

Backed by Supabase project `la-medusa` (ref `qpvykmqepyugqtbxzqnq`, eu-central-1); keys are in config.js (anon key is public by design — Row Level Security protects everything server-side).

- **/account/** (+ /ar/account/) — email+password signup/login for members: live schedule + news feed (members-only items included). First admin: abdghazzawi1@gmail.com (sign up with it to activate).
- **/admin/** — studio management panel (admins only): edit the weekly **Schedule**, post **Events & news** (public banner on home or members-only), upload **Photos** into any photo slot (replaces placeholder art instantly), and add/remove **Admins** by email.
- Public pages pull live data with graceful fallback: if JS/network fails, the static schedule and placeholder art render — nothing breaks on weak internet.
- **Auth config to finish in the Supabase dashboard** (Auth → URL Configuration): set Site URL to the production domain and add it to Redirect URLs, so confirmation/reset emails link correctly.
- Still reserved for Phase 3: `/book/` + payments — `data-book` CTAs flip to it via `bookingEnabled` in config.js.

## Brand

Colors: seafoam `#59B8AF`, aqua `#4CB1A7`, lavender `#846FB7`, soft violet `#6A57A6`, white.
Logo only on white / very light backgrounds (as per brand guidelines pack) — the site's canvas is white by design.
Type: Outfit (sans) + Cormorant Garamond italic (accents); IBM Plex Sans Arabic on AR pages.
