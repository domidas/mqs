import locator.lookup, requests, json, math

def fetch():
  print("Initializing...")

  base_url = "https://api.weather.gov/gridpoints/"

  coordinates = locator.coordLookup()

  # coordLookup returns coordinates as a tuple and possibly negative values. Forecast API call does not accept negatives or floats
  latitude = math.floor(abs(coordinates[0]))
  longitude = math.floor(abs(coordinates[1]))

  office_id = locator.officeLookup()

  # piece URL together and prepare to make calls
  complete_url = base_url + office_id + "/" + str(longitude) + "," + str(latitude) + "/forecast"

  print(complete_url)

  response = requests.get(complete_url)

  x = response.json()
  api_type = (x["type"])

  if x["type"] == "Feature":

    # pull constant geographical data
    elevation = (x["properties"]["elevation"]["value"])

    p = x["geometry"]["coordinates"][0][0]
    latitude = (p[0])
    longitude = (p[1])


    # variable data
    print("Pulling today's metrics...")
    y = x["properties"]["periods"][0]

    # temperature
    current_temp = y["temperature"]
    temp_unit = y["temperatureUnit"]

    # relative humidity
    relative_humidity = y["relativeHumidity"]["value"]

    wind_speed = y["windSpeed"]
    wind_direction = y["windDirection"]

    detailed_forecast = y["detailedForecast"]


    # print following values
    print(" longitude = " +
                str(longitude) +
        "\n latitude = " +                                                                                             
                str(latitude) +
        "\n temperature = " +
                str(current_temp) + temp_unit +
        "\n relative humidity = " +                                                                                                             
                str(relative_humidity) + "%" +
        "\n wind = " +
                str(wind_speed) + " " + wind_direction +
        "\n forecast = " +
                str(detailed_forecast))
  else:
    http_response = str((x["status"]))
    print("ERROR: Unexpected reply. Server replies: " + http_response)
