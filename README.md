# Parklane Residences @ Benoni — Marketing Landing Page

A cinematic, single-page real-estate site for **Parklane Residences @ Benoni** (WSG Group),
a gated lifestyle condominium in Papar, Sabah.

Built as a self-contained static page (`index.html`) and wrapped in a **Streamlit**
app for one-click cloud deployment.

- **Brand:** navy & gold, Playfair Display + Inter
- **Sections:** hero film · overview · the film · residences & unit concepts · facilities · floor plans · location · pricing · specifications · enquiry
- **Content** was extracted from the official sales brochure (`parklane-residences-reference.html`).
- **Media:** cinematic trailer + drone/interior footage + optimised renders and plans.

---

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Then open http://localhost:8501

> `streamlit_app.py` reads `index.html` and inlines every image/video as a base64
> data URI (the component runs in a sandboxed iframe that can't read local files).

## Deploy to Streamlit Community Cloud

1. Push this folder to a GitHub repository.
2. Go to **https://share.streamlit.io** → **New app**.
3. Pick the repo/branch and set **Main file path** to `streamlit_app.py`.
4. **Deploy.** You get a public `https://<app>.streamlit.app` URL.

## Bonus: host as a plain static site (GitHub Pages)

`index.html` uses relative asset paths, so it also works as a static site with
**no** Python — lighter and faster (video is streamed, not inlined):

1. Repo → **Settings → Pages** → Source: `main` / root.
2. Your site: `https://<user>.github.io/<repo>/`.

---

## Structure

```
parklane-residence-site/
├── index.html            # the landing page (self-contained, editable)
├── streamlit_app.py      # Streamlit wrapper (inlines assets → iframe)
├── requirements.txt
├── .streamlit/config.toml
└── assets/
    ├── img/              # optimised renders, floor plans, unit boards, stills
    └── video/            # hero loop + cinematic trailer
```

## Editing content

All copy, prices and contacts live directly in `index.html`. Search for the
section (e.g. `<!-- PRICING -->`) and edit the text. Re-deploy to publish.

---

*Disclaimer: figures, layouts, prices and specifications are from the sales brochure
and are artists' impressions / indicative only, subject to change. Not a contractual
document. © 2026 WSG Group.*
