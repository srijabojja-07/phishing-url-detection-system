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

    features = []

    # Basic features (simple but effective for demo project)
    features.append(0)  # Index placeholder
    features.append(1 if "http" in url else 0)  # UsingIP (simplified)
    features.append(len(url))  # LongURL
    features.append(1 if url.count("/") > 5 else 0)  # ShortURL proxy
    features.append(1 if "@" in url else 0)  # Symbol@
    features.append(1 if "//" in url[8:] else 0)  # Redirecting
    features.append(1 if "-" in url else 0)  # PrefixSuffix
    features.append(url.count("."))  # SubDomains
    features.append(1 if "https" in url else 0)  # HTTPS
    features.append(0)  # DomainRegLen (unknown simplified)
    features.append(0)  # Favicon
    features.append(0)  # NonStdPort
    features.append(0)  # HTTPSDomainURL
    features.append(0)  # RequestURL
    features.append(0)  # AnchorURL
    features.append(0)  # LinksInScriptTags
    features.append(0)  # ServerFormHandler
    features.append(0)  # InfoEmail
    features.append(0)  # AbnormalURL
    features.append(0)  # WebsiteForwarding
    features.append(0)  # StatusBarCust
    features.append(0)  # DisableRightClick
    features.append(0)  # UsingPopupWindow
    features.append(0)  # IframeRedirection
    features.append(0)  # AgeofDomain
    features.append(0)  # DNSRecording
    features.append(0)  # WebsiteTraffic
    features.append(0)  # PageRank
    features.append(0)  # GoogleIndex
    features.append(0)  # LinksPointingToPage
    features.append(0)  # StatsReport

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
    st.rerun()

# -------------------------------
# PREDICTION
# -------------------------------
if predict_button:

    if url == "":
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