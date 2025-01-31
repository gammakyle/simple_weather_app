import requests
import json
import urllib.parse
import tkinter as tk

# Функция, которая будет вызвана при нажатии на кнопку
def change_text():
    label.config(text="Текст изменен!")

def get_weather(lat, lon):
    params = {
        "lat": lat,  # Широта
        "lon": lon,  # Долгота
        "units": "metric",  # Единицы измерения (metric для Цельсия)
        "lang": "ru",  # Язык ответа (русский)
        "appid": 'abe3735b4048823daaf5bd08bdb177d6'  # Ваш API-ключ
    }
    params_str = "&".join([f"{key}={value}" for key, value in params.items()])
    full_url = f"{url_open_weather}?{params_str}"
    print(full_url)

    encoded_params = urllib.parse.urlencode(params)
    url = f"{url_open_weather}?{encoded_params}"

    response = requests.get(url)
    print(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            print(data)
            # Возвращаем координаты первого результата
            return data
        else:
            print("Город не найден.")
            return None
    else:
        print(f"Ошибка: {response.status_code}")
        return None

def get_city_data(city):
    userparams = {
        "q":city,
        "limit":'1',
        "units":'metric',
        "lang":'ru',
        "appid":'abe3735b4048823daaf5bd08bdb177d6'
    }
    
    response = requests.get(url_geocoding, params=userparams)
    response.raise_for_status()
    data = response.json()
    if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
    else:
        print(f"Город '{city}' не найден.")
        return None
    

# Область переменных программы
city = 'Ковров'
url_open_weather = "https://api.openweathermap.org/data/2.5/weather"
url_geocoding = "https://api.openweathermap.org/geo/1.0/direct"
coordinates = get_city_data(city)

# Создаем главное окно
root = tk.Tk()
root.title("Простое приложение на Tkinter")

# Устанавливаем размер окна
root.geometry("600x150")

if coordinates:
    print(coordinates)
    lat, lon = coordinates
    weather_data = get_weather(lat, lon)
    if weather_data:
        # Создаем метку (Label) с начальным текстом
        label = tk.Label(root, text=f"Погода в городе {weather_data['name']}", font=("Arial", 16))
        label.pack(pady=1)  # Размещаем метку в окне с отступом
        label = tk.Label(root, text=f"{weather_data['main']['temp']}°C", font=("Arial", 16))
        label.pack(pady=1)  # Размещаем метку в окне с отступом
    else:
        label = tk.Label(root, text="Простите, не удалось загрузить погоду.", font=("Arial", 16))
        label.pack(pady=1)  # Размещаем метку в окне с отступом
else:
    label = tk.Label(root, text="Простите, не удалось уточнить координаты.", font=("Arial", 16))
    label.pack(pady=1)  # Размещаем метку в окне с отступом

# Запускаем главный цикл обработки событий
root.mainloop()