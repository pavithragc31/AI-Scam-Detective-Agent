# AI Scam Detective Agent

## Overview

AI Scam Detective Agent is an AI-powered cybersecurity system that detects scam messages in SMS, emails, WhatsApp messages, and web content. It uses Google Gemini AI to analyze input text and classify it as SAFE or SCAM.

The system provides a risk score, scam type, explanation, and safety recommendations to help users identify and avoid online fraud in real time.

---

## Problem Statement

With the rapid growth of digital communication, users are frequently targeted by online scams such as phishing messages, fake job offers, OTP fraud, UPI scams, lottery scams, and investment fraud.

These scams are becoming increasingly sophisticated and difficult to detect manually. There is a need for an intelligent system that can automatically analyze messages and detect fraudulent content.

---

## Objectives

- Detect scam messages using AI
- Classify different types of scams
- Provide a risk score from 0 to 100
- Extract URLs, emails, and phone numbers from messages
- Generate safety recommendations
- Improve cybersecurity awareness among users

---

## Features

- AI-based scam detection using Google Gemini
- Scam risk scoring system (0–100)
- Scam type classification (phishing, OTP fraud, UPI scam, etc.)
- URL, email, and phone number extraction
- Real-time message analysis
- Explanation-based AI output
- Streamlit-based interactive UI

---

## System Workflow

1. User inputs a message (SMS, email, WhatsApp text, or URL content)
2. System extracts important entities such as URLs, emails, and phone numbers
3. Cleaned message is sent to Google Gemini AI
4. AI analyzes the content and determines:
   - Safe or Scam classification
   - Scam type
   - Risk score
   - Explanation
   - Safety advice
5. Final result is displayed to the user

---

## Tech Stack

- Python
- Streamlit
- Google Gemini AI
- Google Generative AI API
- Regular Expressions (Regex)
- Natural Language Processing concepts

---

## Project Structure

AI-Scam-Detective/
├── app.py
├── scam_detector.py
├── requirements.txt
├── style.css
├── README.md
│
├── utils/
│   ├── url_checker.py
│   ├── email_checker.py
│   ├── phone_checker.py
│   ├── report_generator.py
│
├── screenshots/
│   ├── safe_message.png
│   ├── scam_message.png

---

## Installation & Setup


### Step 1 :Install Dependencies
pip install -r requirements.txt

### Step 2: Add API Key
Create a .env file and add:
GOOGLE_API_KEY=your_api_key_here

### Step 3: Run Application
streamlit run app.py

---

## Sample Results

### Safe Message
A normal message is classified as SAFE when it contains no suspicious links, urgency, or financial requests.



### Scam Message
A scam message is detected when it contains phishing links, fake urgency, or requests for sensitive personal or financial information.





## Real-World Applications

- Detection of phishing emails
- Prevention of UPI fraud
- Identification of fake job offers
- Scam message filtering
- Cybersecurity awareness system
- Educational AI project for students

---

## Advantages

- Real-time scam detection
- AI-based intelligent decision making
- Easy-to-use interface
- Works on multiple message types
- Improves user safety and awareness

---

## Limitations

- Depends on AI model accuracy
- Requires internet connection
- May not detect newly emerging scam patterns immediately

---

## Future Improvements

- Browser extension for real-time scam detection
- WhatsApp automation integration
- Mobile application version
- Multi-language support
- Voice-based scam alerts
- Improved training dataset for higher accuracy

---

## Conclusion

AI Scam Detective Agent demonstrates the use of Generative AI in cybersecurity. It helps users detect scam messages, understand risks, and stay protected from online fraud. The system provides clear explanations and risk scoring, making it useful for real-world applications and cybersecurity awareness.

---

## Author

Pavithra G C
Computer science student (PES UNIVERCITY)