import streamlit as st
import pandas as pd
import joblib
from urllib.parse import urlparse
import re

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Phishing URL Detection System",
    page_icon="🚨",
    layout="centered"
)

# -------------------------------
# LOAD MODEL
# -------------------------------
model = joblib.load("models/phishing_model.pkl")

# -------------------------------
# FEATURE EXTRACTION (FIXED)
# -------------------------------
def extract_features(url):

    parsed = urlparse(url)

    # EXACT FEATURE COUNT = 31 (matches your model structure)
    features = [

        0,  # Index

        1 if re.match(r"^http[s]?://\d+\.\d+\.\d+\.\d+", url) else 0,  # UsingIP

        1 if len(url) > 75 else 0,  # LongURL

        1 if len(url) < 20 else 0,  # ShortURL

        1 if "@" in url else 0,  # Symbol@

        1 if url.count("//") > 1 else 0,  # Redirecting//

        1 if "-" in parsed.netloc else 0,  # PrefixSuffix-

        parsed.netloc.count("."),  # SubDomains

        1 if url.startswith("https") else 0,  # HTTPS

        0,  # DomainRegLen
        0,  # Favicon
        0,  # NonStdPort
        0,  # HTTPSDomainURL
        0,  # RequestURL
        0,  # AnchorURL
        0,  # LinksInScriptTags
        0,  # ServerFormHandler
        0,  # InfoEmail
        0,  # AbnormalURL
        0,  # WebsiteForwarding
        0,  # StatusBarCust
        0,  # DisableRightClick
        0,  # UsingPopupWindow
        0,  # IframeRedirection
        0,  # AgeofDomain
        0,  # DNSRecording
        0,  # WebsiteTraffic
        0,  # PageRank
        0,  # GoogleIndex
        0,  # LinksPointingToPage
        0   # StatsReport
    ]

    return features

# -------------------------------
# TITLE
# -------------------------------
st.title("🚨 Phishing URL Detection System")
st.write("Enter a URL to check if it is SAFE or PHISHING")

st.markdown("---")

# -------------------------------
# URL INPUT (WITH KEY FIX)
# -------------------------------
url = st.text_input("🔗 Enter URL", key="url_input")

# -------------------------------
# BUTTONS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    predict_button = st.button("🚨 Check URL")

with col2:
    reset_button = st.button("🔄 Reset")

# -------------------------------
# RESET FIX (PROPER)
# -------------------------------
if reset_button:
    st.session_state["url_input"] = ""
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