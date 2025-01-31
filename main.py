import requests
import tkinter as tk

# Функция, которая будет вызвана при нажатии на кнопку
def change_text():
    label.config(text="Текст изменен!")

def get_weather(lat, lon):
    params = {
        "lat": lat,  # Широта
        "lon": lon,  # Долгота
        "appid": 'abe3735b4048823daaf5bd08bdb177d6',  # Ваш API-ключ
        "units": "metric",  # Единицы измерения (metric для Цельсия)
        "lang": "ru"  # Язык ответа (русский)
    }

    response = requests.get(url_geocoding, params=params)

    if response.status_code == 200:
        data = response.json()
        if data:
            # Возвращаем координаты первого результата
            return data[0]["lat"], data[0]["lon"]
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
        "lang":'ru',
        "appid":'abe3735b4048823daaf5bd08bdb177d6'
    }
    params_str = "&".join([f"{key}={value}" for key, value in userparams.items()])
    full_url = f"{url_open_weather}?{params_str}"

    print(full_url)
    
    response = requests.get(url_open_weather, params=userparams)
    if response.status_code == 200:
        weather_data = response.json()
        return(weather_data)
    else:
        print(f"Ошибка: {response.status_code}")
        return None
    

# Область переменных программы
city = 'Ковров'
url_open_weather = "http://api.openweathermap.org/data/3.0/weather"
url_geocoding = "http://api.openweathermap.org/geo/1.0/direct"
coordinates = get_city_data(city)

# Создаем главное окно
root = tk.Tk()
root.title("Простое приложение на Tkinter")

# Устанавливаем размер окна
root.geometry("600x150")

if coordinates:
    lat, lon = coordinates
    weather_data = get_weather(lat, lon)
    if weather_data:
        # Создаем метку (Label) с начальным текстом
        label = tk.Label(root, text="Погода в городе {city}", font=("Arial", 16))
        label.pack(pady=1)  # Размещаем метку в окне с отступом
        label = tk.Label(root, text="Погода в городе {city}", font=("Arial", 16))
        label.pack(pady=1)  # Размещаем метку в окне с отступом
    else:
        label = tk.Label(root, text="Простите, не удалось загрузить погоду.", font=("Arial", 16))
        label.pack(pady=1)  # Размещаем метку в окне с отступом
else:
    label = tk.Label(root, text="Простите, не удалось уточнить координаты.", font=("Arial", 16))
    label.pack(pady=1)  # Размещаем метку в окне с отступом

# Запускаем главный цикл обработки событий
root.mainloop()