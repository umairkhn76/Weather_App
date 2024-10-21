import tkinter as tk
import requests

def weather():
    city=e.get()
    url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f88403a40483cf9686b8a5aa31458ff9"
    data=requests.get(url).json()
    temp=int(data['main']['temp']-273.15)
    min_temp=int(data['main']['temp_min']-273.15)
    max_temp=int(data['main']['temp_max']-273.15)
    humidity=data['main']['humidity']
    wind=data['wind']['speed']
    pressure=data['main']['pressure']
    f="Tempreature is "+str(temp)+"°C "
    total="Min temp is "+str(min_temp)+"\n"+"pressure is "+str(pressure)+"\n"+"Max temp is "+str(max_temp)+"\n"+"Wind speed is "+str(wind)+"\n"+"Humidity is "+str(humidity)
    lab.config(text=f)
    lab.config(text=total)
    

win = tk.Tk()
win.geometry("500x500")
win.title("Weather App")
win.config(bg="pink")

lab=tk.Label(win,text="Enter the name of the city",font=("poppins",30,"bold"),bg="White",fg="black")
lab.place(x=60,y=20,height=50,width=380)

e=tk.Entry(font=("Poppins",30,"bold"),bg="White",fg="black")
e.pack(pady=80)
e.focus()