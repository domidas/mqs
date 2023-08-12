import caller.forecast
print("Welcome to the Meteorological Query System")
print("1: Forecast Query \n\
2: Radar Query")
choice = str(input())

if choice == "1":
  caller.forecast.fetch()
if choice == "2":
    print("Not ready yet...")
