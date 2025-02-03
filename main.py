from openweather_logics import *
from tk_gen import *


# Функция, которая будет вызвана при нажатии на кнопку

# Область переменных программы
city = 'Ковров'
coordinates = get_city_data(city)
alert_message = "Неизвестная ошибка"

if coordinates:
    lat, lon = coordinates
    weather_data = get_weather(lat, lon)
    if weather_data:
        create_main_window(weather_data)        
    else:
        alert_message = "не удалость выполнить запрос на погоду"
        create_alert_window(alert_message)
else:
    alert_message = "не удалость выполнить запрос на координаты"
    create_alert_window(alert_message)