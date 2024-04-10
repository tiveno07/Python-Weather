import requests 
from dotenv import load_dotenv 
import os 
from pprint import pprint


load_dotenv()

def get_current_weather(city):     
    
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"
    
    weather_data = requests.get(request_url).json()
    # pprint(weather_data)
    
    return weather_data

if __name__ == "__main__":
    print("\n****  Get Current Weather Conditions *****\n")
    
    city = input("\nPlease enter a city name.")
    
    #Checking for empty strips or string wth only spaces
    if not bool(city.strip()): 
        city = "Lagos"
    
    weather_data = get_current_weather(city)
    
    print("\n")
    pprint(weather_data)
