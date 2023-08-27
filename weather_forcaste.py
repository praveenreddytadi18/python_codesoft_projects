from tkinter import *
import requests
import time

def getWeather():
    city=text.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cb3f147cc45fee38a5e3cee029566180"
    json_data = requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    min_temp=int(json_data['main']['temp_min']-273.15)
    max_temp=int(json_data['main']['temp_max']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))
    sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-21600))
    final_info=condition+"\n "+ str(temp)+" °C"
    final_data="\n"+"maximum temp: "+str(max_temp)+"\n"+"minimum temp: "+str(min_temp)+"\n"+"Pressure: "+str(pressure)+"\n"+"Sunrise: "+str(sunrise)+"\n"+"Sunset: "+str(sunset)
    
    label1.config(text=final_info)
    label2.config(text=final_data)
    
root=Tk()
root.geometry("600x500")
root.title("Weather")

f=(15)
t=(35)



text=Entry(root,font=t)
text.pack(pady=20)
text.focus()

search=Button(root,text="search",command=getWeather).pack()


label1 = Label(root, font=t)
label1.pack()
label2 = Label(root, font=f)
label2.pack()
root.mainloop()
