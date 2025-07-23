import streamlit as st
import json
from openai import OpenAI
from geopy.geocoders import Nominatim
import requests
from datetime import datetime

geolocator = Nominatim(user_agent="location_finder")

def get_location_and_weather(latitude, longitude, client):
    """
    Function to find city, state, and country based on user's geolocation and fetch weather data.
    
    Parameters:
        openai_key (str): OpenAI API key.
        weather_api_key (str): OpenWeatherMap API key.
    
    Returns:
        dict: Weather data and location information.
    """
    geolocator = Nominatim(user_agent="location_finder")


    location = geolocator.reverse((latitude, longitude), language="en")

    address = location.raw.get('address', {})
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')


    location = f"{city}, {state}, {country}"

    coor_message = f"""
    This is the location {location}, format it in a way so that it is accepted by 
    openweathermap API example if the location is "City of Syracuse,New York, United States"
    format it as "Syracuse, US", if just "New York,New York,United States" format it as
    "New York City, US" and only return the formatted location nothing else.
    """

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": coor_message},
                    {"role": "user", "content": location}]
    )

    location = stream.choices[0].message.content


    data, local_time = get_weather(location)
        
    
    return data, local_time, location

def get_weather(formatted_location):
    
    urlbase = "https://api.openweathermap.org/data/2.5/"
    urlweather = f"weather?q={formatted_location}&appid={st.secrets['weather_key']}"
    url = urlbase + urlweather

    response = requests.get(url)
    data = response.json()

    utc_timestamp = data['dt']
    offset_seconds = data['timezone']
    local_timestamp = utc_timestamp + offset_seconds
    local_time = datetime.fromtimestamp(local_timestamp)

    return data, local_time
