import json
import tkinter

import requests
import random
import time
from tkinter import *
tk = Tk()
def kelvinConverter(temp):
    fahrenheit = (float(temp)-273.15)*9/5+32
    return str(int(fahrenheit))
def findWeather(textbox):
    url = ("http://api.openweathermap.org/data/2.5/weather?q="+textbox+"&appid=a1bfeaa007e1c7608ea96baf58b7cc4c")
    r = requests.get(url)
    Label(tk,text="________").pack()
    Label(tk, text=textbox+":").pack()
    for pair in r.json()['main']:
        Label(tk,text=str(pair)+": "+kelvinConverter(str(r.json()['main'][str(pair)]))).pack()
    Label(tk, text="________").pack()

def clicked():
    findWeather(e.get())

tk.title("WeatherFinder")
tk.geometry("500x700")
e = Entry(tk, width = 50)
e.insert(0,"Enter Your City")
e.pack()
button = Button(tk, width=35,text="Confirm", command=clicked)
button.pack()

#just put in the name of your city and it shows you the weather details thanks to the openweather api


mainloop()