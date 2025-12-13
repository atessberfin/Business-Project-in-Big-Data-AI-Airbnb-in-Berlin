import base64
from pathlib import Path
from PIL import Image
import streamlit as st

BASE = Path(__file__).parent
IMAGES = BASE / "images"

# ---- FAVICON ----
try:
    favicon = Image.open(IMAGES / "home.png")
except Exception:
    favicon = "🏠"

st.set_page_config(
    page_title="Smart Pricing & Investment",
    page_icon=favicon,
    layout="wide"
)

# ---- SESSION STATE ----
if "role" not in st.session_state:
    st.session_state.role = None

# ---- HELPERS ----
def img_tag(p: Path, alt: str = "", size: int = 108) -> str:
    data = p.read_bytes()
    b64 = base64.b64encode(data).decode()
    return f"""
    <div class="icon-circle" style="width:{size}px;height:{size}px;">
        <img src="data:image/png;base64,{b64}" alt="{alt}">
    </div>
    """

# ---- DARK PREMIUM THEME ----
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">

<style>
/* Streamlit üst bar/menü/alt yazıları kapat */
[data-testid="stHeader"] {display: none;}
[data-testid="stToolbar"] {display: none;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* ---- Base ---- */
.stApp {
    background: radial-gradient(1200px 700px at 20% 10%, rgba(20,184,166,0.18), rgba(0,0,0,0)),
                radial-gradient(900px 600px at 90% 20%, rgba(99,102,241,0.16), rgba(0,0,0,0)),
                #0b1220;
    color: #e5e7eb;
    font-family: 'Inter', sans-serif;
}

section[data-testid="stSidebar"] {
    background: rgba(2,6,23,0.75) !important;
    border-right: 1px solid rgba(148,163,184,0.18);
}

/* Sayfanın üst boşluğunu azalt + ortalı max genişlik */
.block-container {
    padding-top: 3.2rem;
    padding-bottom: 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
}

/* ---- Typography ---- */
.hero-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 46px;
    line-height: 1.05;
    margin-top: 12px;
    margin-bottom: 10px;
    letter-spacing: 0.3px;
    color: #f8fafc;
}

.hero-subtitle {
    text-align: center;
    font-size: 16px;
    color: rgba(226,232,240,0.78);
    margin-bottom: 28px;
}

/* ---- Circular icon (Host / Investor) ---- */
.icon-circle {
    border-radius: 50%;
    background: rgba(15, 23, 42, 0.55);
    border: 1px solid rgba(148,163,184,0.35);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 14px auto;
    box-shadow:
        inset 0 0 0 1px rgba(255,255,255,0.04),
        0 10px 30px rgba(0,0,0,0.35);
}

.icon-circle img {
    width: 56%;
    height: 56%;
    object-fit: contain;
    filter: invert(1);
    opacity: 0.92;
}

/* ---- Buttons ---- */
div[data-testid="stButton"] > button {
    width: 100%;
    border-radius: 14px;
    padding: 0.85rem 1rem;
    border: 1px solid rgba(148,163,184,0.22);
    background: rgba(2, 6, 23, 0.35);
    color: #e5e7eb;
    font-weight: 600;
    transition: transform 0.15s ease, box-shadow 0.15s ease, border 0.15s ease;
}

div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px);
    border: 1px solid rgba(20,184,166,0.55);
    box-shadow: 0 12px 40px rgba(0,0,0,0.35);
}

/* Alt boşluk */
.role-spacer { height: 10px; }

/* =========================================================
   ✅ Kart stili (st.container(border=True))
   ========================================================= */
div[data-testid="stVerticalBlockBorderWrapper"]{
    border-radius: 22px !important;
    padding: 26px 22px 18px 22px !important;
    background: rgba(17, 24, 39, 0.55) !important;
    border: 1px solid rgba(148,163,184,0.20) !important;
    box-shadow: 0 18px 60px rgba(0,0,0,0.35) !important;
    backdrop-filter: blur(10px);
    text-align: center; /* kart içindeki her şeyi ortala */
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover{
    border-color: rgba(20,184,166,0.55) !important;
    box-shadow:
        inset 0 0 0 1px rgba(255,255,255,0.06),
        0 14px 40px rgba(20,184,166,0.22) !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] > div:empty {
    display: none !important;
}

/* =========================================================
   ✅ İSTEDİĞİN DEĞİŞİKLİK: Host / Investor yazısı
   ========================================================= */
.role-label {
    font-family: 'Inter', sans-serif;
    font-weight: 800;       /* KALIN */
    font-size: 20px;
    margin-top: 12px;
    margin-bottom: 6px;
    color: #f8fafc;
    text-align: center;     /* ORTALI */
    letter-spacing: 0.3px;
}

.role-desc {
    font-size: 14px;
    color: rgba(226,232,240,0.75);
    text-align: center;     /* ORTALI */
    line-height: 1.45;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown('<div class="hero-title">Berlin Airbnb Pricing Studio</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Smart pricing, what-if scenarios, and listing assistance for <b>Hosts</b> and <b>Investors</b>.</div>',
    unsafe_allow_html=True
)

# ---- ROUTING ----
def landing():
    left_spacer, colHost, colInvestor, right_spacer = st.columns([1, 2, 2, 1], gap="large")

    with colHost:
        with st.container(border=True):
            st.markdown(img_tag(IMAGES / "rent.png", "HOST", size=110), unsafe_allow_html=True)
            st.markdown('<div class="role-label">Host</div>', unsafe_allow_html=True)
            st.markdown('<div class="role-desc">Predict an optimal nightly rate and generate a compelling listing description.</div>', unsafe_allow_html=True)
            if st.button("Continue as Host →", key="btn_host"):
                st.session_state.role = "host"
                st.rerun()

    with colInvestor:
        with st.container(border=True):
            st.markdown(img_tag(IMAGES / "property.png", "INVESTOR", size=110), unsafe_allow_html=True)
            st.markdown('<div class="role-label">Investor</div>', unsafe_allow_html=True)
            st.markdown('<div class="role-desc">Estimate revenue, yield, and run occupancy scenarios before you invest.</div>', unsafe_allow_html=True)
            if st.button("Continue as Investor →", key="btn_investor"):
                st.session_state.role = "investor"
                st.rerun()

    st.markdown('<div class="role-spacer"></div>', unsafe_allow_html=True)


def host_page_placeholder():
    top = st.columns([1, 3, 1])
    with top[0]:
        if st.button("← Back", key="back_from_host"):
            st.session_state.role = None
            st.rerun()
    st.subheader("🏠 Host Workspace")
    st.write("Buraya birazdan Property Details formu + Price Card + 3-bullet özet + What-if + Listing Assistant gelecek.")


def investor_page_placeholder():
    top = st.columns([1, 3, 1])
    with top[0]:
        if st.button("← Back", key="back_from_investor"):
            st.session_state.role = None
            st.rerun()
    st.subheader("💼 Investor Workspace")
    st.write("Buraya birazdan yatırım inputları + revenue/yield kartları + scenario grafiği gelecek.")


if st.session_state.role is None:
    landing()
elif st.session_state.role == "host":
    host_page_placeholder()
elif st.session_state.role == "investor":
    investor_page_placeholder()
