import sys
import re

def redact_pii(text):
    # Redact Emails
    text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[REDACTED - EMAIL]', text)
    # Redact Phone Numbers (Standard formats)
    text = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', '[REDACTED - PHONE]', text)
    # Redact SSNs
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[REDACTED - SSN]', text)
    # Redact IPv4 Addresses
    text = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[REDACTED - IP]', text)
    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide text to anonymize.")
        sys.exit(1)
        
    user_text = sys.argv[1]
    print("\n### 🛡️ Scrubbed Text\n")
    print(redact_pii(user_text))