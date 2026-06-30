import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import SYSTEM_PROMPT


load_dotenv()


API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set.")


genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.5-flash")


def detect_scam(text):
    prompt = f"{SYSTEM_PROMPT}\n\nMessage:\n{text}"

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error while analyzing the message:\n\n{e}"