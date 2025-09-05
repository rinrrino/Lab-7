solution.py
`python
#!/usr/bin/env python3
# solution.py — Lab-7 (API, using OpenWeatherMap as example)
import os, sys, requests

def get_weather(city):
    key = os.environ.get('OWM_API_KEY')
    if not key:
        print("Set OWM_API_KEY environment variable.")
        return
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': key, 'units': 'metric', 'lang':'ru'}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    j = r.json()
    out = {
        'city': j.get('name'),
        'weather': j['weather'][0]['description'],
        'temp': j['main']['temp'],
        'pressure': j['main']['pressure'],
        'humidity': j['main']['humidity']
    }
    return out

if name == 'main':
    city = sys.argv[1] if len(sys.argv)>1 else 'Saint Petersburg'
    try:
        w = get_weather(city)
        if w:
            print(f"{w['city']}: {w['weather']}, {w['temp']}°C, {w['humidity']}% humidity, {w['pressure']} hPa")
    except Exception as e:
        print("Error:", e)
