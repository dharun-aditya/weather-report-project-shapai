import requests,sys
from datetime import datetime

report=sys.stdout

api_key = 'c6f4c22d818f80725e8cdde8aad2e919'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
time = datetime.now().strftime("%d-%m-%Y_%I-%M-%S%p")
sys.stdout = open("weather_repo_"+time+".txt",'w')
print ("-------------------------------------------------------------")
print ("Current Weather at - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Temperature         : {:.2f} deg C".format(temp))
print ("Weather description :",weather_desc)
print ("Wind                :",wind ,'km/ph')
print ("Humidity            :",hmdt, '%')


sys.stdout = report
sys.stdout.close()

