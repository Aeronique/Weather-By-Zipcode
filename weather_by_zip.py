import os
import requests
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()  # read .env
    raw = os.getenv("OPENWEATHER_API_KEY")
    if not raw:
        raise RuntimeError("No key found in OPENWEATHER_API_KEY")
    return raw.strip()

def fetch_weather(zipcode, country="us"):
    api_key = get_api_key()
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "zip": f"{zipcode},{country}",
        "appid": api_key,
        "units": "imperial"
    }

    resp = requests.get(url, params=params)
    if resp.status_code == 401:
        print("⚠️ Your API key isn’t active yet. Please wait a couple hours and try again.")
        return None

    resp.raise_for_status()
    return resp.json()

def pretty_print(weather_json):
    name = weather_json["name"]
    cond = weather_json["weather"][0]["description"].title()
    temp = weather_json["main"]["temp"]
    feels = weather_json["main"]["feels_like"]
    humidity = weather_json["main"]["humidity"]

    print(f"\nCurrent weather in {name}:")
    print(f"  Conditions: {cond}")
    print(f"  Temperature: {temp:.1f}°F (feels like {feels:.1f}°F)")
    print(f"  Humidity: {humidity}%\n")

def main():
    zipcode = input("Enter ZIP code (e.g. 10001): ").strip()
    data = fetch_weather(zipcode)
    if data is None:
        print("No data to display—please try again later.")
        return

    pretty_print(data)

if __name__ == "__main__":
    main()
