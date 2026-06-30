import re

def extract_phone_numbers(text):
    pattern = r"\+?\d[\d\s-]{8,15}"
    return re.findall(pattern, text)