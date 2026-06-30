import streamlit as st
import re

from scam_detector import detect_scam
from utils.url_checker import extract_urls, suspicious_urls
from utils.email_checker import extract_emails
from utils.phone_checker import extract_phone_numbers
from utils.report_generator import generate_report

# CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="AI Scam Detective",
    page_icon="",
    layout="wide"
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("AI Model", "Gemini 2.5")
c2.metric("Threat Types", "10+")
c3.metric("Languages", "100+")
c4.metric("Accuracy", "AI Powered")

st.markdown("""
Detect phishing emails, fake lottery messages, WhatsApp scams, UPI fraud,
fake job offers and suspicious websites using Gemini AI.
""")

text = st.text_area(
    "Paste suspicious message",
    height=220,
    placeholder="Paste Email / SMS / WhatsApp / Website text..."
)

if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter a message.")
        st.stop()

    with st.spinner("Gemini AI is investigating..."):
        result = detect_scam(text)

    st.success("Investigation Completed")

    # ---------------- AI REPORT ----------------
    st.subheader("AI Investigation Report")

    st.write(result)

    match = re.search(r"Scam Score:\s*(\d+)", result)

    if match:
        score = int(match.group(1))

        st.progress(score)

        if score >= 80:
            st.error(f"High Risk ({score}/100)")
        elif score >= 50:
            st.warning(f"Medium Risk ({score}/100)")
        else:
            st.success(f"Low Risk ({score}/100)")

        report = generate_report(result)

        st.download_button(
            "Download Report",
            report,
            file_name="scam_report.txt",
            mime="text/plain"
        )

    # ---------------- URL CHECK ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("URLs")

        urls = extract_urls(text)

        if urls:
            for url in urls:
                st.code(url)

            bad = suspicious_urls(urls)

            if bad:
                st.error("Suspicious URL Found")
            else:
                st.success("No suspicious URL pattern detected.")
        else:
            st.info("No URLs found.")

    with col2:
        st.subheader("Emails")

        emails = extract_emails(text)

        if emails:
            for email in emails:
                st.code(email)
        else:
            st.info("No email addresses found.")

        st.subheader("Phone Numbers")

        phones = extract_phone_numbers(text)

        if phones:
            for phone in phones:
                st.code(phone)
        else:
            st.info("No phone numbers found.")


st.divider()

st.markdown("""
### Features
- Scam Detection using Gemini AI  
- URL Detection  
- Email Detection  
- Phone Number Detection  
- Download Investigation Report  

                
THANK YOU, STAY SAFE, ALL THE BEST""")