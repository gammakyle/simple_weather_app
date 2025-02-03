import requests
import urllib.parse

url_open_weather = "https://api.openweathermap.org/data/2.5/weather"
url_geocoding = "https://api.openweathermap.org/geo/1.0/direct"

#---------------------#
def getapi_fun():
    api_file = open('api_keyfile.txt','r')
    api_key = api_file.readline()
    api_file.close()
    return api_key
#---------------------#

#---------------------#
def get_city_data(city):
    userparams = {
        "q":city,
        "limit":'1',
        "units":'metric',
        "lang":'ru',
        "appid": getapi_fun()  # Ваш API-ключ
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
#---------------------#

#---------------------#
def get_weather(lat, lon):
    params = {
        "lat": lat,  # Широта
        "lon": lon,  # Долгота
        "units": "metric",  # Единицы измерения (metric для Цельсия)
        "lang": "ru",  # Язык ответа (русский)
        "appid": getapi_fun()  # Ваш API-ключ
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
#---------------------#