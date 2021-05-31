import tkinter as tk
import requests
import time

def weather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    
    json_data = requests.get(api).json()
    cond = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    minTemp = int(json_data['main']['temp_min'] - 273.15)
    maxTemp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = cond + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(minTemp) + "°C" + "\n" + "Max Temp: " + str(maxTemp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n"  + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas= tk.Tk()
canvas.geometry("700x600")
canvas.title("Weather App")

f = ("poppins", 25, "bold")
t = ("poppins", 45, "bold")

textfield =  tk.Entry(canvas, font = t)
textfield.pack(pady =20)
textfield.focus()
textfield.bind('<Return>', weather)


label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()

