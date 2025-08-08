# main.py
from email_checker import check_email_breaches

def main():
    raw = input("Skriv inn e-postadresser (skilt med komma): ")
    emails = [e.strip() for e in raw.split(",") if e.strip()]

    for email in emails:
        print(f"\n🔎 Sjekker {email} …")
        try:
            breaches = check_email_breaches(email)
            if breaches:
                print(f"🚨 '{email}' er involvert i disse lekkasjene:")
                for b in breaches:
                    print(f"   • {b['Name']} (lekket: {b['BreachDate']})")
            else:
                print(f"✅ Ingen lekkasjer funnet for '{email}'")
        except Exception as e:
            print(f"❌ Feil for '{email}': {e}")

if __name__ == "__main__":
    main()
