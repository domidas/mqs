#this is a very simplistic test but I've yet to see it lie
import requests, json

url = "https://api.weather.gov"

response = requests.get(url)
x = response.json()

status = x["status"]

print("API reports: " + status + "!")
