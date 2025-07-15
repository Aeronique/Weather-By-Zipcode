# Weather-By-Zipcode
A super simple Python script to fetch current weather information by U.S. ZIP code.

# Features

Fetches current weather conditions (temperature, humidity, description) for a ZIP code.

Gracefully handles API key activation wait times.

Minimal dependencies: requests and python-dotenv.

# Prerequisites

Python 3.8 or higher

A free API key from OpenWeatherMap

# Installation

Clone the repository (replace <username> and <repo> with the correct values):

git clone https://github.com/<username>/<repo>.git
cd <repo>

# Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate    # macOS/Linux
# .\venv\Scripts\Activate.ps1  # Windows PowerShell

# Install dependencies:

pip install -r requirements.txt

# Configure your API key:

Copy .env.example to .env:

cp .env.example .env

Edit .env and replace YOUR_API_KEY with your actual key:

OPENWEATHER_API_KEY=YOUR_API_KEY

# Usage

Run the script:

python3 weather_by_zip.py

When prompted, enter a U.S. ZIP code (e.g., 10001).

Example output:

Enter ZIP code (e.g. 10001): 90210

Current weather in Beverly Hills:
  Conditions: Clear Sky
  Temperature: 75.2°F (feels like 74.5°F)
  Humidity: 45%

# Troubleshooting

401 Unauthorized: If you see a message about the API key not being active, wait a few hours for OpenWeatherMap to propagate the key.

Environment variable issue: Ensure .env is in the project root and contains the correct key. Activate your virtual environment before running the script.
