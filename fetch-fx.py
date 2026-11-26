import requests

url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/"
response = requests.get(url, params={"date": "2026-11-26"}, timeout=30)
data = response.json()

for currency in data[0]["currencies"]:
    if currency["code"] == "USD":
        print("USD:", currency["rate"])