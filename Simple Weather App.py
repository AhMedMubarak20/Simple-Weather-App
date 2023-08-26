import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Weather in {city}: {weather_description}")
    print(f"Temperature: {temperature}°C")

city_name = input("Enter city name: ")
get_weather(city_name)
