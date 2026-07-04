"""
Parklane Residences @ Benoni — marketing landing page (Streamlit wrapper).

Renders the self-contained index.html. On Streamlit the component runs inside a
sandboxed iframe, so local asset paths can't be resolved at runtime — we inline
every image/video as a base64 data URI before handing the HTML to the iframe.

The same index.html also works as a plain static site (e.g. GitHub Pages), where
the relative asset paths resolve directly and no inlining is needed.
"""
import base64
import mimetypes
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

st.set_page_config(
    page_title="Parklane Residences @ Benoni · WSG Group",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip Streamlit chrome/padding so the page reads full-bleed.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility:hidden;}
      .stApp {background:#0a1a2e;}
      .block-container {padding:0 !important; max-width:100% !important;}
      [data-testid="stAppViewContainer"] > .main {padding:0;}
      section.main > div {padding:0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

# For the inlined iframe build, swap the heavy trailer for the lite version.
INLINE_SWAPS = {"assets/video/trailer.mp4": "assets/video/trailer-lite.mp4"}


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


@st.cache_data(show_spinner="Preparing residence…")
def build_page() -> str:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    # Replace every referenced asset path (in src=, poster=, and lb('…') calls)
    # with an inlined data URI. Longest paths first to avoid partial overlaps.
    rel_paths = sorted(
        {str(p.relative_to(ROOT)).replace("\\", "/") for p in ASSETS.rglob("*") if p.is_file()},
        key=len,
        reverse=True,
    )
    for rel in rel_paths:
        src = INLINE_SWAPS.get(rel, rel)
        if rel in html:
            html = html.replace(rel, data_uri(ROOT / src))
    return html


# Tall enough to fit the whole desktop page so the parent window scrolls
# (no nested scrollbox); scrolling=True keeps narrow/mobile layouts usable.
components.html(build_page(), height=11800, scrolling=True)
