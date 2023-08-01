
import requests

def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check the response status code
    if response.status_code == 200:
        # Parse the response data in JSON format
        data = response.json()
        
        # Extract the temperature in Kelvin from the data
        temperature_kelvin = data['main']['temp']
        
        # Convert temperature from Kelvin to Celsius
        temperature_celsius = temperature_kelvin - 273.15
        
        # Display the temperature to the user
        print(f"The current temperature in {city_name} is {temperature_celsius:.2f}°C.")
    else:
        print("Error in fetching data. Please check your API key or city name.")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    api_key = "46f68f5f588db4903d6163e2416e8d50"

    get_weather(city_name, api_key)

