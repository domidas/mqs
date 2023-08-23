import requests, json, urllib.parse

base_url = "https://geocoding.geo.census.gov/geocoder/locations/address?"

address = "110 Elm St"
zipcode = "66952"

print("Using address " + address + " and zipcode " + zipcode)

formatted_address = urllib.parse.quote_plus(address)

complete_url = base_url + "street=" + formatted_address + "&zip=" + zipcode +   "&benchmark=Public_AR_Current" + "&format=json"

try:
  response = requests.get(complete_url, timeout=30)
except ConnectTimeout:
  print("Timed out after 30 seconds")

x = response.json()

if "status" in x:
  status = x(["status"])
  error = x(["errors"][0])
  print("ERROR: Unexpected reply. Server replies status " + status + " with error message " + error)
elif ["addressMatches"] != []:
  print("Successful reply. Geocoding API operational.")
    
