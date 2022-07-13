import requests
import json
API_KEY="d56c8f69033661adb7ab6298b3df2444"
city=input("Enter city name:")
URL=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
res=requests.get(URL)
json_data=json.loads(res.text)
weather=json_data["weather"][0]["description"]
temprature=json_data["main"]["temp"]
humidity=json_data["main"]["humidity"]
wind_speed=json_data["wind"]["speed"]

print(f"weather:{weather}")
print(f"temprature:{temprature}")
print(f"humidity:{humidity}")
print(f"wind speed:{wind_speed}")