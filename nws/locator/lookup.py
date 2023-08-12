import requests, json, urllib.parse 
from .cache import Cache

def coordLookup():

  base_url = "https://geocoding.geo.census.gov/geocoder/locations/address?"

  # the cache functions do NOT use return. This is so I don't have to type return each time for each condition (file does/does not exist, file will/will not be used
  # coordLookup just reads the cached file.
  Cache.addressCacheCheck()

  cache_file = open("./address.txt", mode='r')
  cache_file_contents = address_file.readlines()
  address = cache_file_contents[0]
  zipcode = cache_file_contents[1]

  #address = input("Please enter an address: ")
  #zipcode = input("Please enter the corresponding zip code: ")

  # make spaces in address +'s 
  formatted_address = urllib.parse.quote_plus(address)

  complete_url = base_url + "street=" + formatted_address + "&zip=" + zipcode +   "&benchmark=Public_AR_Current" + "&format=json"

  #print(complete_url)

  response = requests.get(complete_url)
  x = response.json()

  # check if request is valid and address is found
  if "status" in x:
    status = x(["status"])
    error = x(["errors"][0])
    print("ERROR: Unexpected reply. Server replies status " + status + " with error message " + error)
  elif x["result"]["addressMatches"] == []:
    print("Address not found.")

  #print(x)

  p = x["result"]["addressMatches"][0]["coordinates"]
  global latitude
  global longitude
  latitude = (p["y"])
  longitude = (p["x"])

  return latitude, longitude

# finds the specific forecasting office for a particular gridpoint
def officeLookup():
    
  points_url = "https://api.weather.gov/points/" + str(latitude) + "," + str(longitude)
  response = requests.get(points_url)
  x = response.json()

  if "status" in x:
      status = x(["status"])
      detail = x(["detail"])
      print("ERROR: Unexpected reply. Server replies status " + status + " with error message " + detail)

  office_id = x["properties"]["gridId"]
  print("The Forecasting Office ID for your area is: " + office_id)
  return office_id
