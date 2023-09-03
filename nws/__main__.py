import os, caller.forecast 
from locator.lookup import Lookup
print("Welcome to the Meteorological Query System")
print("1: Forecast Query \n\
2: Radar Query")
choice = str(input())

if choice == "1":
  # need to figure out a way to make it to where if cache exists, don't ask for address or something idk
  address = input("Please enter an address: ")
  zipcode = input("Please enter the corresponding zip code: ")
  coordinates = Lookup.coordLookup(address, zipcode)
  office_id = Lookup.officeLookup(coordinates)
  caller.forecast.fetch(coordinates, office_id)
if choice == "2":
    print("Not ready yet...")
