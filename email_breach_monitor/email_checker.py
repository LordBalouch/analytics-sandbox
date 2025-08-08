# email_checker.py
import os
from dotenv import load_dotenv

load_dotenv()
HIBP_API_KEY = os.getenv("HIBP_API_KEY", "").strip()

# Demo-database for offline-testing med generiske e-poster
DEMO_DB = {
    "your.email+positive@example.com": [
        {
            "Name": "DemoBreachService",
            "BreachDate": "2025-07-01",
            "Description": "Simulert datalekkasje for demo-formål."
        }
    ],
    "your.email+negative@example.com": []
}

def check_email_breaches(email):
    # Hvis du senere vil bruke ekte API, kan du legge logikken under her:
    if HIBP_API_KEY:
        # ekte HIBP-kall kommer her
        pass

    # -------------------------------
    # Lokal demo-modus uten eksternt kall
    print("⚠️ Kjører LOKAL DEMO-modus (ingen eksternt kall).")
    return DEMO_DB.get(email, [])
