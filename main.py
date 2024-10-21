from tkinter import *
from PIL import Image, ImageTk
import requests


def get_quote():
    url = 'https://api.whatdoestrumpthink.com/api/v1/quotes/random/'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    quote = data["message"]
    canvas.itemconfig(quote_text, text=quote, font=("Arial", 20, "bold"))


def resize_image(image, percentage):
    width, height = image.size
    new_width = int(width * (percentage / 100))
    new_height = int(height * (percentage / 100))
    return image.resize((new_width, new_height))


window = Tk()
window.title("Tronald Dump Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Tronald Dump Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

original_image = Image.open('trump-stupid.jpg')
resize_percentage = 30  # Change this value as needed
resized_image = resize_image(original_image, resize_percentage)
photo = ImageTk.PhotoImage(resized_image)
trump_button = Button(image=photo, highlightthickness=0, command=get_quote)
trump_button.grid(row=1, column=0)


window.mainloop()
