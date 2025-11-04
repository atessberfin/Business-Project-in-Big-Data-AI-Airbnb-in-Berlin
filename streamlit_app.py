import os
import streamlit as st

st.set_page_config(
    page_title="Smart Pricing & Investment",
    page_icon="/workspaces/Business-Project-in-Big-Data-AI-Airbnb-in-Berlin/images/home.png",
    layout="wide"
)

# ABSOLUTE PATHS
RENT_PATH = "/workspaces/Business-Project-in-Big-Data-AI-Airbnb-in-Berlin/images/rent.png"
PROP_PATH = "/workspaces/Business-Project-in-Big-Data-AI-Airbnb-in-Berlin/images/property.png"

# ---------- STYLES ----------
st.markdown("""
    <style>
    .top-center {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        margin-top: 60px;
        gap: 60px;
    }
    .card {
        text-align: center;
        border: 2px solid #ccc;
        border-radius: 20px;
        padding: 25px;
        width: 180px;
        transition: all 0.3s ease;
    }
    .card:hover {
        box-shadow: 0 0 15px rgba(0,0,0,0.2);
        transform: translateY(-5px);
    }
    .card img {
        width: 100px;
        height: 100px;
        object-fit: contain;
    }
    .label {
        font-weight: bold;
        margin-top: 10px;
        color: #222;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- CONTENT ----------
st.markdown('<div class="top-center">', unsafe_allow_html=True)

st.markdown('''
    <div class="card">
        <img src="RENT_PATH">
        <div class="label">HOST</div>
    </div>
''', unsafe_allow_html=True)

st.markdown('''
    <div class="card">
        <img src="PROP_PATH">
        <div class="label">INVESTOR</div>
    </div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)