from tkinter import *
import requests
from PIL import Image, ImageTk


def get_quote():
    response = requests.get(url="https://api.quotable.io/random")
    response.raise_for_status()
    quote = response.json()['content']
    canvas.itemconfig(quote_text, text = quote)

    #Write your code here.



window = Tk()
window.title("Lurtz Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Lurtz* Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

original_lurtz =  Image.open("lurtz.png")
resized_image = original_lurtz.resize((100, 100), Image.LANCZOS) 
lurtz_img = ImageTk.PhotoImage(resized_image)
lurtz_button = Button(image=lurtz_img, highlightthickness=0, command=get_quote)
lurtz_button.grid(row=1, column=0)

get_quote()

window.mainloop()