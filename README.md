# Benoni Township · Parklane Residences — Design 02 “Township in Depth”

Second web-page design for **WSG Group 美嘉城集團**, presenting the **entire Benoni
Township** (Papar, Sabah) with Parklane Residences at its centre.

## What makes this design different from Design 01

- **3D scroll website technique** (GSAP ScrollTrigger):
  - Opening **bilingual WSG Group logo sting** — an AI-animated gold light-sweep
    over the WSG GROUP | 美嘉城集團 logo on navy marble.
  - Hero with an AI-generated **township aerial fly-through video**.
  - A pinned **deep-zoom journey**: five full-frame scenes (masterplan → mall →
    facilities deck → lakeside park → township at night) fly toward the camera
    in true 3D perspective as you scroll.
  - Pinned **horizontal glide** through the township pillars (mall 148k sf,
    Servay, 10Star Cinemas, North Borneo University, shop-offices, lake park).
  - Parallax sky-deck scene, 3D-tilt unit cards, 3D-entrance film frames,
    count-up stats.
- **Fully bilingual** EN / 繁體中文 toggle (persists via localStorage).
- Navy & gold WSG brand palette; Playfair Display + Inter + Noto Serif TC.

## AI-generated assets (Higgsfield AI MCP)

`assets/gen/`:

| File | What it is |
|---|---|
| `logo-scene.jpg` | Bilingual WSG logo re-staged on navy marble (Nano Banana 2, 2K) |
| `logo-sting-web.mp4` | 5 s animated logo reveal (Kling 3.0 Turbo, 1080p) |
| `township-hero.jpg` | Township masterplan aerial, 21:9, extended from the real render |
| `township-fly-web.mp4` | 8 s aerial fly-through of the township (Kling 3.0 Turbo, 1080p) |
| `mall-boulevard.jpg` | Street-level mall / cinema boulevard at dusk |
| `sky-deck.jpg` | Central facilities deck at twilight |
| `night-skyline.jpg` | Township at night, 21:9 |
| `park-lifestyle.jpg` | Lakeside park morning lifestyle |
| `story-web.mp4` | 38 s bilingual story film “Begin Your Home Journey” — 7 scenes (aerial dream → park → mall → home → deck → night → WSG logo end-card), Higgsfield scenes + ffmpeg crossfades + licensed instrumental score |
*(web-optimised versions in the repo; raw 2K PNG / 1080p masters kept locally)*

All were generated with the project's **real renders as references** so the
architecture stays faithful. Real floor plans, unit boards, interior renders
and drone films are reused from Design 01 (`assets/img`, `assets/rooms`,
`assets/video`).

## Run locally

**As the Streamlit app (same as the cloud deployment):**

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

`streamlit_app.py` inlines every referenced asset as a base64 data URI and pins
the component iframe to the full viewport (100dvh) so the scroll-driven 3D
scenes work inside Streamlit's sandboxed iframe.

**Or as a plain static site:**

```bash
python -m http.server 8541 --directory .
```

then open http://localhost:8541 (internet needed for Google Fonts + GSAP CDN).

## Mobile-first optimisations

- **Page weight ~5.6 MB total** (down from ~78 MB of raw AI assets): all
  generated stills served as optimised progressive JPEGs (≤1920 px), hero
  fly-through re-encoded 30 MB → 3 MB, logo sting 6.3 MB → 0.8 MB
  (`*-web.mp4`, faststart). Raw PNG/MP4 masters kept alongside.
- **Hamburger menu** with full-screen navy overlay (numbered serif links +
  WhatsApp CTA) under 900 px; nav brand compacts.
- **3D journey plates go portrait (4:5)** on phones so each scene fills the
  screen as it flies toward the camera.
- **Hero title floats cinematically** on touch devices (replaces the desktop
  mouse-parallax).
- **Connectivity map is swipeable** on phones (pre-centred on the Parklane hub,
  "swipe the map" hint) so labels stay readable; floor plans pan horizontally.
- `100svh` viewport units (no URL-bar jump), no horizontal page overflow,
  ≥44 px tap targets, videos `muted playsinline` for iOS autoplay.

## Facts encoded in the page

4 towers · 19 storeys · 999-year tenure · 36 months to completion* ·
100% Bank Islam financing* · 2-bed 620/680 sf from RM 246,000 ·
3-bed 1,000–1,100 sf from RM 378,000 · WhatsApp enquiry +60 19-899 2313.
*Subject to the developer's latest announcement.
