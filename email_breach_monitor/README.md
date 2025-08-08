## Demo Mode

I denne første versjonen kjører `Email Breach Monitor` i **lokal demo-modus** uten eksternt API:

- Alle e-postadresse-sjekker går mot en innebygd `DEMO_DB` i `email_checker.py`.  
- Bruk generiske e-poster i demo:  
  - `your.email+positive@example.com` (simulert lekkasje)  
  - `your.email+negative@example.com` (ingen lekkasje)  
- Når du vil bytte til ekte API, fyller du inn `HIBP_API_KEY` i `.env` og setter inn API-kallet i `email_checker.py`.

### Slik tester du demo-modusen

```bash
pip install -r requirements.txt
python main.py
# Skriv inn:
your.email+positive@example.com, your.email+negative@example.com
