import streamlit as st
import pandas as pd
import joblib

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
# RESET LOGIC
# -------------------------------
if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

# -------------------------------
# TITLE
# -------------------------------
st.title("🚨 Phishing URL Detection System")

st.write(
    "Enter phishing feature values to detect whether the website is Legitimate or Phishing."
)

st.markdown("---")

# -------------------------------
# USER INPUTS
# -------------------------------

UsingIP = st.number_input(
    "UsingIP",
    value=0,
    key=f"UsingIP_{st.session_state.reset_counter}"
)

LongURL = st.number_input(
    "LongURL",
    value=0,
    key=f"LongURL_{st.session_state.reset_counter}"
)

ShortURL = st.number_input(
    "ShortURL",
    value=0,
    key=f"ShortURL_{st.session_state.reset_counter}"
)

Symbol = st.number_input(
    "Symbol@",
    value=0,
    key=f"Symbol_{st.session_state.reset_counter}"
)

Redirecting = st.number_input(
    "Redirecting//",
    value=0,
    key=f"Redirecting_{st.session_state.reset_counter}"
)

PrefixSuffix = st.number_input(
    "PrefixSuffix-",
    value=0,
    key=f"PrefixSuffix_{st.session_state.reset_counter}"
)

SubDomains = st.number_input(
    "SubDomains",
    value=0,
    key=f"SubDomains_{st.session_state.reset_counter}"
)

HTTPS = st.number_input(
    "HTTPS",
    value=0,
    key=f"HTTPS_{st.session_state.reset_counter}"
)

DomainRegLen = st.number_input(
    "DomainRegLen",
    value=0,
    key=f"DomainRegLen_{st.session_state.reset_counter}"
)

Favicon = st.number_input(
    "Favicon",
    value=0,
    key=f"Favicon_{st.session_state.reset_counter}"
)

NonStdPort = st.number_input(
    "NonStdPort",
    value=0,
    key=f"NonStdPort_{st.session_state.reset_counter}"
)

HTTPSDomainURL = st.number_input(
    "HTTPSDomainURL",
    value=0,
    key=f"HTTPSDomainURL_{st.session_state.reset_counter}"
)

RequestURL = st.number_input(
    "RequestURL",
    value=0,
    key=f"RequestURL_{st.session_state.reset_counter}"
)

AnchorURL = st.number_input(
    "AnchorURL",
    value=0,
    key=f"AnchorURL_{st.session_state.reset_counter}"
)

LinksInScriptTags = st.number_input(
    "LinksInScriptTags",
    value=0,
    key=f"LinksInScriptTags_{st.session_state.reset_counter}"
)

ServerFormHandler = st.number_input(
    "ServerFormHandler",
    value=0,
    key=f"ServerFormHandler_{st.session_state.reset_counter}"
)

InfoEmail = st.number_input(
    "InfoEmail",
    value=0,
    key=f"InfoEmail_{st.session_state.reset_counter}"
)

AbnormalURL = st.number_input(
    "AbnormalURL",
    value=0,
    key=f"AbnormalURL_{st.session_state.reset_counter}"
)

WebsiteForwarding = st.number_input(
    "WebsiteForwarding",
    value=0,
    key=f"WebsiteForwarding_{st.session_state.reset_counter}"
)

StatusBarCust = st.number_input(
    "StatusBarCust",
    value=0,
    key=f"StatusBarCust_{st.session_state.reset_counter}"
)

DisableRightClick = st.number_input(
    "DisableRightClick",
    value=0,
    key=f"DisableRightClick_{st.session_state.reset_counter}"
)

UsingPopupWindow = st.number_input(
    "UsingPopupWindow",
    value=0,
    key=f"UsingPopupWindow_{st.session_state.reset_counter}"
)

IframeRedirection = st.number_input(
    "IframeRedirection",
    value=0,
    key=f"IframeRedirection_{st.session_state.reset_counter}"
)

AgeofDomain = st.number_input(
    "AgeofDomain",
    value=0,
    key=f"AgeofDomain_{st.session_state.reset_counter}"
)

DNSRecording = st.number_input(
    "DNSRecording",
    value=0,
    key=f"DNSRecording_{st.session_state.reset_counter}"
)

WebsiteTraffic = st.number_input(
    "WebsiteTraffic",
    value=0,
    key=f"WebsiteTraffic_{st.session_state.reset_counter}"
)

PageRank = st.number_input(
    "PageRank",
    value=0,
    key=f"PageRank_{st.session_state.reset_counter}"
)

GoogleIndex = st.number_input(
    "GoogleIndex",
    value=0,
    key=f"GoogleIndex_{st.session_state.reset_counter}"
)

LinksPointingToPage = st.number_input(
    "LinksPointingToPage",
    value=0,
    key=f"LinksPointingToPage_{st.session_state.reset_counter}"
)

StatsReport = st.number_input(
    "StatsReport",
    value=0,
    key=f"StatsReport_{st.session_state.reset_counter}"
)

st.markdown("---")

# -------------------------------
# BUTTONS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    predict_button = st.button("🚨 Check URL")

with col2:
    reset_button = st.button("🔄 Reset")

# -------------------------------
# RESET BUTTON
# -------------------------------
if reset_button:
    st.session_state.reset_counter += 1
    st.rerun()

# -------------------------------
# PREDICTION
# -------------------------------
if predict_button:

    input_data = pd.DataFrame([[

        0,
        UsingIP,
        LongURL,
        ShortURL,
        Symbol,
        Redirecting,
        PrefixSuffix,
        SubDomains,
        HTTPS,
        DomainRegLen,
        Favicon,
        NonStdPort,
        HTTPSDomainURL,
        RequestURL,
        AnchorURL,
        LinksInScriptTags,
        ServerFormHandler,
        InfoEmail,
        AbnormalURL,
        WebsiteForwarding,
        StatusBarCust,
        DisableRightClick,
        UsingPopupWindow,
        IframeRedirection,
        AgeofDomain,
        DNSRecording,
        WebsiteTraffic,
        PageRank,
        GoogleIndex,
        LinksPointingToPage,
        StatsReport

    ]], columns=[

        'Index',
        'UsingIP',
        'LongURL',
        'ShortURL',
        'Symbol@',
        'Redirecting//',
        'PrefixSuffix-',
        'SubDomains',
        'HTTPS',
        'DomainRegLen',
        'Favicon',
        'NonStdPort',
        'HTTPSDomainURL',
        'RequestURL',
        'AnchorURL',
        'LinksInScriptTags',
        'ServerFormHandler',
        'InfoEmail',
        'AbnormalURL',
        'WebsiteForwarding',
        'StatusBarCust',
        'DisableRightClick',
        'UsingPopupWindow',
        'IframeRedirection',
        'AgeofDomain',
        'DNSRecording',
        'WebsiteTraffic',
        'PageRank',
        'GoogleIndex',
        'LinksPointingToPage',
        'StatsReport'

    ])

    prediction = model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.error("⚠️ Phishing Website Detected")
    else:
        st.success("✅ Legitimate Website")