import streamlit as st
import pandas as pd
import joblib
import os
from urllib.parse import urlparse

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Phishing URL Detection System",
    page_icon="🚨",
    layout="centered"
)

# -------------------------------
# LOAD MODEL (SAFE PATH)
# -------------------------------
model = joblib.load("models/phishing_model.pkl")

# -------------------------------
# FEATURE EXTRACTION FROM URL
# -------------------------------
def extract_features(url):

    import re
    from urllib.parse import urlparse

    parsed = urlparse(url)

    features = []
    features.append(0)
    features.append(1 if re.match(r"^http[s]?://\d+\.\d+\.\d+\.\d+", url) else 0)
    features.append(1 if len(url) > 75 else 0)
    features.append(1 if len(url) < 20 else 0)
    features.append(1 if "@" in url else 0)
    features.append(1 if url.count("//") > 1 else 0)
    features.append(1 if "-" in parsed.netloc else 0)
    features.append(parsed.netloc.count("."))
    features.append(1 if url.startswith("https") else 0)

    for _ in range(22):
        features.append(0)

    return features

# -------------------------------
# TITLE
# -------------------------------
st.title("🚨 Phishing URL Detection System")
st.write("Enter a URL and the system will detect if it is SAFE or PHISHING")

st.markdown("---")

# -------------------------------
# URL INPUT
# -------------------------------
url = st.text_input("🔗 Enter URL")

# -------------------------------
# BUTTONS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    predict_button = st.button("🚨 Check URL")

with col2:
    reset_button = st.button("🔄 Reset")

# -------------------------------
# RESET
# -------------------------------
if reset_button:
    st.session_state.clear()
    st.rerun()

# -------------------------------
# PREDICTION
# -------------------------------
if predict_button:

    if url.strip() == "":
        st.warning("Please enter a URL")

    else:
        features = extract_features(url)
        input_data = pd.DataFrame([features])

        prediction = model.predict(input_data)

        st.markdown("---")

        if prediction[0] == 1:
            st.error("⚠️ Phishing Website Detected")
        else:
            st.success("✅ Legitimate Website")