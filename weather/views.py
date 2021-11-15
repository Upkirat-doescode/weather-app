from django.shortcuts import render
from .models import city
from .forms import cityform
import requests
# Create your views here.
def index(request):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=178dcda4a6812bd0e66f63ec5e9fa7b5"
    if request.method=="POST":
        form=cityform(request.POST)
        form.save()
    form=cityform()
    cuidad=city.objects.all()
    alltheinfo=[]
    for i in cuidad:
        url1=requests.get(url.format(i)).json()
        cityweather={
            "city":i.name,
            "temperature":url1["main"]["temp"],
            "description":url1["weather"][0]["description"],
            "icon":url1["weather"][0]["icon"]
        }
        alltheinfo.append(cityweather)
    x={
        "alltheinfo":alltheinfo,
        "form":form
    }
    return render(request,"weather/weather.html",x)