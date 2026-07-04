"""
Benoni Township · Parklane Residences — Design 02 "Township in Depth"
(Streamlit wrapper).

Renders the self-contained index.html. On Streamlit the component runs inside a
sandboxed iframe, so local asset paths can't be resolved at runtime — we inline
every referenced image/video as a base64 data URI before handing the HTML to
the iframe.

Unlike the previous design, this page is a scroll-driven 3D experience
(GSAP ScrollTrigger with pinned scenes), so the iframe must be a real scrolling
viewport: we render it at 100dvh and let the page scroll *inside* the iframe
instead of stretching the iframe to the page's full height.

The same index.html also works as a plain static site (e.g. GitHub Pages),
where the relative asset paths resolve directly and no inlining is needed.
"""
import base64
import mimetypes
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

st.set_page_config(
    page_title="Benoni Township · Parklane Residences — WSG Group 美嘉城集團",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip Streamlit chrome/padding and pin the component iframe to the full
# viewport — the 3D-scroll site scrolls inside it.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility:hidden;}
      .stApp {background:#081120;}
      .block-container {padding:0 !important; max-width:100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding:0;}
      section.main > div {padding:0 !important;}
      div[data-testid="stCustomComponentV1"], .stApp iframe {
        height: 100vh !important;
        height: 100dvh !important;
        width: 100% !important;
        display: block;
        border: 0;
      }
      [data-testid="stVerticalBlock"] {gap:0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


@st.cache_data(show_spinner="Preparing the township…")
def build_page() -> str:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    # Replace every referenced asset path (src=, poster=, CSS url(...)) with an
    # inlined data URI. Longest paths first to avoid partial overlaps.
    rel_paths = sorted(
        {str(p.relative_to(ROOT)).replace("\\", "/") for p in ASSETS.rglob("*") if p.is_file()},
        key=len,
        reverse=True,
    )
    for rel in rel_paths:
        if rel in html:
            html = html.replace(rel, data_uri(ROOT / rel))
    return html


# height is a fallback only — the CSS above pins the iframe to 100dvh and the
# site scrolls internally (required for the pinned 3D scroll scenes).
components.html(build_page(), height=900, scrolling=True)
