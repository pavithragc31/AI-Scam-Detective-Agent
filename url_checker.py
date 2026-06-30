import re


def extract_urls(text):
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)


def suspicious_urls(urls):
    suspicious = []

    keywords = [
        "claim",
        "verify",
        "login",
        "secure",
        "gift",
        "reward",
        "bank",
        "free",
        "winner",
        "bonus",
        "prize"
    ]

    for url in urls:
        lower = url.lower()

        if any(word in lower for word in keywords):
            suspicious.append(url)

        elif ".xyz" in lower:
            suspicious.append(url)

        elif ".top" in lower:
            suspicious.append(url)

        elif ".click" in lower:
            suspicious.append(url)

        elif ".live" in lower:
            suspicious.append(url)

    return suspicious