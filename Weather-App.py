import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        
        print(f"The City is: {city}")
        print(f"The Temperature is: {temp}°C")
        print(f"The Weather is: {weather_desc}")
        print(f"The Humidity is: {humidity}%")
    else:
        print(f"The City {city} not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
