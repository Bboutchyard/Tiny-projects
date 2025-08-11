import requests
from bs4 import BeautifulSoup

# Ask user for location
city = input("Enter a city name: ").strip()
state = input("Enter a state (or leave blank if outside US): ").strip()

# Build URL — wttr.in accepts "city,state" format
location = f"{city},{state}" if state else city
url = f"https://wttr.in/{location}?format=j1"

# Avoid Brotli by removing "br" from Accept-Encoding
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate"
}

# Fetch JSON data from wttr.in
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    exit()

data = response.json()

# Extract weather details
current = data["current_condition"][0]
temp_f = current["temp_F"]
weather_desc = current["weatherDesc"][0]["value"]
wind_mph = current["windspeedMiles"]
humidity = current["humidity"]

# Print results
print(f"\nWeather for {city}, {state}")
print(f"Temperature: {temp_f}°F")
print(f"Condition: {weather_desc}")
print(f"Wind Speed: {wind_mph} mph")
print(f"Humidity: {humidity}%")