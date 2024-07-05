import requests
from tkinter import *

# response = requests.get("http://api.open-notify.org/iss-now.json")

# data = response.json()
# longitute = data['iss_position']["longitude"]
# print(longitute)

# https://api.kanye.rest



# def get_quote():
#     response = requests.get("https://api.kanye.rest")
#     data = response.json()
#     kanye_quote = data['quote']
#     canvas.itemconfig(quote_text,text=kanye_quote)
    
#     #Write your code here.



# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="image/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 13, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="image/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)



# window.mainloop()



# https://api.sunrise-sunset.org/json

parameters = {
    "lat": 14.058324,
    "lng" : 108.277199
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
print(data)