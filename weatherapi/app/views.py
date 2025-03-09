from django.shortcuts import render
import requests
# Create your views here.
def  index(request):
    a = None
    if request.method == "POST":
        city = request.POST.get('city')
        data = requests.get(f'https://goweather.herokuapp.com/weather/{city}')
        a = data.json()
    return render(request, 'index.html',{'data':a})