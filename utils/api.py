import requests

def znajdz_lokalizacje(nazwa):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": nazwa, "format": "json", "countrycodes": "pl", "limit": 1}
    headers = {"User-Agent": "pogoda-app"}
    res = requests.get(url, params=params, headers=headers)
    return res.json()[0]

def pobierz_dane_godzinowe(lat, lon, data):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,precipitation,relative_humidity_2m,windspeed_10m"
        f"&start_date={data}&end_date={data}&timezone=auto"
    )
    return requests.get(url).json()["hourly"]
