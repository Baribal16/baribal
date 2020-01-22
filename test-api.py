import requests
p = {"lat":50.7098734, "lon":4.5088394, "appid":"bf74ee8fc00719b66aa042e25dae7a2c"}
r = requests.get('https://samples.openweathermap.org/data/2.5/weather?', params=p)

API_respons = r.json()

temp = (API_respons["main"]["temp"]) - 273.15
print(temp)