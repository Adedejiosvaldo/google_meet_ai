import re

CORRECTIONS = {
    "favor": "Favour",
    "Ages": "Angels",
    "ages of favor": "Angels of Favour",
    "messiah": "Mercy",
    "merci": "Mercy",
    "zabito": "Favour",
    "zabo": "Favour",
    "it surrounds him every day": "it's erupting from within",
    "opening up for me": "opening doors for me"
}

def correct_text(text):
    text_lower = text.lower()
    for wrong, right in CORRECTIONS.items():
        if wrong.lower() in text_lower:
            text = re.sub(re.escape(wrong), right, text, flags=re.IGNORECASE)
    return text
