import tkinter as tk
from tkinter import ttk
from style_config import *

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

#---------------------#
def create_main_window(weather_data):
    main_window = tk.Tk()
    configure_styles()
    main_window.resizable(width=False, height=False)
    main_window.title("Погода")
    main_window.geometry("300x100")
    label = ttk.Label(main_window, text=f"Погода в городе {weather_data['name']}", style = "TLabel")
    label.pack(pady=1)  # Размещаем метку в окне с отступом
    label = ttk.Label(main_window, text=f"{weather_data['main']['temp']}°C", style = "TLabel")
    label.pack(pady=1)  # Размещаем метку в окне с отступом
    # Кнопка для открытия второго окна
    # Запуск главного цикла
    main_window.mainloop()
#---------------------#
#---------------------#
def create_alert_window(alert_message):
    alert_window = tk.Tk()
    configure_styles()
    alert_window.resizable(width=False, height=False)
    alert_window.title("Что-то пошло не так...")
    alert_window.geometry("400x20")
    label = ttk.Label(alert_window, text=f"Ошибка: {alert_message}", style = "TLabel")
    label.pack(pady=1)  # Размещаем метку в окне с отступом
    center_window(alert_window)
    alert_window.mainloop()
#---------------------#

