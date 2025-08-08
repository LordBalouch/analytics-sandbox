# test_email_checker.py
import os
import pytest
from email_checker import check_email_breaches

def test_demo_positive(monkeypatch):
    # Fjern API-key for å tvinge demo-modus
    monkeypatch.delenv("HIBP_API_KEY", raising=False)
    result = check_email_breaches("your.email+positive@example.com")
    assert isinstance(result, list)
    # Sjekk at det finnes en demo-lekkasje for denne
    assert any(b["Name"] == "DemoBreachService" for b in result)

def test_demo_negative(monkeypatch):
    monkeypatch.delenv("HIBP_API_KEY", raising=False)
    result = check_email_breaches("your.email+negative@example.com")
    # Denne skal gi tom liste
    assert result == []

@pytest.mark.parametrize("email", [
    "your.email+positive@example.com",
    "your.email+negative@example.com",
    "unknown@example.com"
])
def test_demo_db_keys(monkeypatch, email):
    monkeypatch.delenv("HIBP_API_KEY", raising=False)
    result = check_email_breaches(email)
    # Sjekk at returtypen alltid er en liste
    assert isinstance(result, list)
