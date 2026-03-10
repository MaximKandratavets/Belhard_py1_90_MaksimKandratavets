"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

import requests

API_KEY = "ваш_ключ_от_OpenWeatherMap"

city = input("Введите город: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
response = requests.get(url)
data = response.json()

if response.status_code == 200:  # проверяем, что город найден
    print("="*40)
    print(f"Погода в городе: {data['name']}")
    print("="*40)
    
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    
    print(f"Температура:     {temp}°C")
    print(f"Ощущается как:  {feels_like}°C")
    print(f"Влажность:       {humidity}%")
    print(f"Погодные условия:{description}")
    print(f"Скорость ветра:  {wind_speed} м/с")
    print("="*40)
else:
    print("Город не найден или ошибка запроса")