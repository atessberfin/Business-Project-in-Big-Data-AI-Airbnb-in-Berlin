import os
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

# ---- HELPER FUNCTION ----
def img_tag(p: Path, alt: str = "") -> str:
    data = p.read_bytes()
    b64 = base64.b64encode(data).decode()
    return f'<img src="data:image/png;base64,{b64}" alt="{alt}">'


# ---- STYLE ----
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>
body, [class*="stApp"], .stApp {
    background-color: #DFEBF6 !important;
    font-family: 'Poppins', sans-serif;
}

section[data-testid="stSidebar"] {
    background-color: #DFEBF6 !important;
}

/* Başlıklar */
h1 {
    text-align: center;
    color: #29353C;
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 46px;
    margin-top: 40px;
    margin-bottom: 10px;
    letter-spacing: 0.8px;
}
h4 {
    text-align: center;
    color: #29353C;
    font-family: 'Poppins', sans-serif;
    font-weight: 300;
    font-style: italic;
    font-size: 20px;
    margin-bottom: 70px;
}

/* Kartlar */
.card {
  text-align: center;
  border: none;
  border-radius: 22px;
  padding: 35px;
  width: 220px;
  transition: all .3s ease;
  background-color: #ffffff;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}
.card:hover {
  box-shadow: 0 6px 25px rgba(41,53,60,0.35);
  transform: translateY(-8px);
  background-color: #ECF4FB;
}
.card img {
  width: 120px;
  height: 120px;
  object-fit: contain;
}
.label {
  font-weight: 600;
  margin-top: 14px;
  color: #29353C;
  letter-spacing: 0.5px;
  font-size: 17px;
  font-family: 'Poppins', sans-serif;
  text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<h1>Smart Pricing & Investment Advisor</h1>
<h4><i>Find the optimal rental price or discover your next real estate opportunity.</i></h4>
""", unsafe_allow_html=True)

# ---- CONTENT ----
col_empty_left, col_host, col_investor, col_empty_right = st.columns([2, 1, 1, 2])

with col_host:
    st.markdown(
        f"""
        <div class="card">
          {img_tag(IMAGES / "rent.png", "HOST")}
          <div class="label">HOST</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_investor:
    st.markdown(
        f"""
        <div class="card">
          {img_tag(IMAGES / "property.png", "INVESTOR")}
          <div class="label">INVESTOR</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
