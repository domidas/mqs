import requests, json, urllib.parse 
from .cache import Cache

class Lookup:
    
  def coordLookup(address, zipcode):
    
    # check to see if cache exists
    while Cache.check_cache() == True:
        cached_coords = Cache.read_cache()
        ch = input("Cached coordinates found. Do you wish to use " + str(cached_coords) + "? [Y/N]: ").upper()

        if ch == "Y":
            return cached_coords
        elif ch == "N":
            Cache.delete_cache()

    base_url = "https://geocoding.geo.census.gov/geocoder/locations/address?"

    # make spaces in address +'s
    formatted_address = urllib.parse.quote_plus(address)

    complete_url = base_url + "street=" + formatted_address + "&zip=" + zipcode +   "&benchmark=Public_AR_Current" + "&format=json"

    print(complete_url)

    response = requests.get(complete_url)
    x = response.json()

    # check if request is valid and address is found
    if "status" in x:
      status = x(["status"])
      error = x(["errors"][0])
      print("ERROR: Unexpected reply. Server replies status " + status + " with error message " + error)
    elif x["result"]["addressMatches"] == []:
      print("Address not found.")

    p = x["result"]["addressMatches"][0]["coordinates"]

    latitude = (p["y"])
    longitude = (p["x"])

    #dictionary for lat and long
    coordinates = {
      "latitude": latitude,
      "longitude": longitude
     }

    # cache coordinates
    Cache.write_cache(coordinates)

    return coordinates

  # finds the specific forecasting office for a particular gridpoint
  def officeLookup(coordinates):

    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]

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
