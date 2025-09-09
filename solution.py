# solution.py

import requests
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk
from io import BytesIO

def weather():
    print("=== Task 1: Погода ===")
    city_name = "Moscow"
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Погода в {city_name}:")
        print("Температура:", data['main']['temp'], "°C")
        print("Влажность:", data['main']['humidity'], "%")
        print("Давление:", data['main']['pressure'], "hPa")
        print("Состояние:", data['weather'][0]['description'])
        print("Скорость ветра:", data['wind']['speed'], "м/с")
    else:
        print("Ошибка API:", response.status_code)


def fox_generator():
    print("=== Доп. задание: генератор картинок ===")

    def change_image():
        response = requests.get("https://randomfox.ca/floof/")
        img_url = response.json()['image']
        img_response = requests.get(img_url)
        img_data = Image.open(BytesIO(img_response.content))
        img_tk = ImageTk.PhotoImage(img_data)
        label.config(image=img_tk)
        label.image = img_tk

    root = Tk()
    root.title("Random Fox Generator")
    label = Label(root)
    label.pack()
    btn = Button(root, text="Следующая картинка", command=change_image)
    btn.pack()
    change_image()
    root.mainloop()

if name == "main":
    weather()
    fox_generator()
