# 🚨 Phishing URL Detection System

## 📌 Project Overview

The **Phishing URL Detection System** is a Machine Learning-based cybersecurity project developed to identify whether a website is **Legitimate** or **Phishing** based on various URL and website security features.

The system utilizes a trained **Random Forest Classifier** to analyze phishing-related characteristics and provide accurate predictions through an interactive **Streamlit web application**.

---

## 🎯 Problem Statement

Phishing websites are one of the most common cyber threats used to steal sensitive information such as usernames, passwords, banking credentials, and personal data.

Traditional users often find it difficult to distinguish between legitimate and malicious websites. This project aims to assist users by automatically classifying websites using machine learning techniques.

---

## 🚀 Key Features

* Machine Learning-based phishing detection
* Random Forest Classification Model
* Interactive Streamlit Web Interface
* Real-time Prediction System
* Feature-based Website Analysis
* Reset Functionality for Multiple Predictions
* User-Friendly Interface
* GitHub and Streamlit Deployment

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib

### Machine Learning

* Random Forest Classifier

### Development Tools

* VS Code
* Git
* GitHub
* Streamlit Cloud

---

## 📊 Machine Learning Model

### Algorithm Used

**Random Forest Classifier**

### Model Purpose

The model was trained using phishing website feature datasets containing multiple cybersecurity-related indicators.

### Features Considered

The model analyzes website characteristics such as:

* Using IP Address
* Long URL
* Short URL
* Symbol (@)
* Redirecting (//)
* Prefix-Suffix (-)
* Subdomains
* HTTPS Usage
* Domain Registration Length
* Favicon
* Non-Standard Port
* Request URL
* Anchor URL
* Server Form Handler
* Website Traffic
* Page Rank
* Google Index
* DNS Records
* Website Forwarding
* And other phishing-related security indicators

---

## 📂 Project Structure

```text
phishing-url-detection-system/
│
├── dataset/                # Dataset used for model training
├── notebooks/              # Model training and experimentation notebooks
├── models/
│   └── phishing_model.pkl  # Trained Random Forest model
│
├── app/
│   └── app.py              # Streamlit application
│
├── screenshots/            # Application screenshots
├── Presentation/           # Internship presentation files
├── Secure_Coding_Review/   # Security review report
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/srijabojja-07/phishing-url-detection-system.git
```

### 2️⃣ Navigate to Project Directory

```bash
cd phishing-url-detection-system
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit Application

```bash
streamlit run app/app.py
```

---

## 🎯 Prediction Results

The application provides the following outputs:

### ✅ Legitimate Website

Indicates that the website exhibits characteristics commonly associated with safe and trusted websites.

### ⚠️ Phishing Website Detected

Indicates that the website contains suspicious features commonly found in phishing attacks.

---

## 📸 Application Preview

Screenshots of the application interface and prediction results are available in the **screenshots** folder.

---

## 🎓 Internship Deliverables

This project was developed as part of the **CodeAlpha Cyber Security Internship**.

Additional deliverables included:

* Phishing Awareness Presentation
* Secure Coding Review Report
* Machine Learning-based Phishing Detection System

---

## 🔮 Future Enhancements

* Real-time URL Feature Extraction
* Advanced Feature Engineering
* Browser Extension Integration
* API-based Threat Intelligence Integration
* Enhanced User Interface
* Multi-Model Comparison

---

## 👩‍💻 Author

**Srija Bojja**

B.Tech – Information Technology

Cybersecurity & Machine Learning Enthusiast

GitHub: https://github.com/srijabojja-07
