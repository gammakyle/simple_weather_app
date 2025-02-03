import tkinter as tk
from tkinter import ttk

def configure_styles():
    style = ttk.Style()
    # Стиль для кнопок
    style.configure("TButton",
                    font=("Arial", 12),
                    padding=10,
                    background="#4CAF50",
                    foreground="white")
    style.map("TButton",
              background=[("active", "#45a049")])
    # Стиль для меток
    style.configure("TLabel",
                    font=("Arial", 10),
                    foreground="#333")
    # Стиль для полей ввода
    style.configure("TEntry",
                    font=("Arial", 12),
                    padding=5,
                    foreground="#333",
                    fieldbackground="#f0f0f0")
    # Стиль для фреймов
    style.configure("TFrame",
                    background="white")