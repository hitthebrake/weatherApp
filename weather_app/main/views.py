from django.shortcuts import render, redirect
import datetime
import requests

def home(request, city='astana'):
    WEATHER_API = 0# Drag your API here
    if request.method=="POST" and 'city' in request.POST:
        return redirect('home', city=request.POST["city"])
    
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}"

        
    PARAMS = { "units":"metric" }

    try:
        data = requests.get(weather_url, PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity = data['main']['humidity']

        day = datetime.date.today()

        return render(request, "main/main.html", { "throwed":False, "description":description, "icon":icon, "temp":temp, "humidity":humidity, "day":day, "city":city })
    except KeyError:
        return redirect('home')
        
        

# Create your views here.
