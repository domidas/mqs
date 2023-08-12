import os

class Cache:
  def __init__(self, address, zipcode):
    

  def addressCacheCreate(self):
    address_file = open("./address.txt", mode='w')
    address = input("Please enter a street address: ")
    zipcode = input("Please enter a zipcode: ")
    address_file.write(address + "\n" + zipcode)

  def addressCacheCheck(self):
    while os.path.isfile("./address.txt") == False:
      print("No address cached. Making new file...")
      .addressCacheCreate()
      quit()
    
    address_file = open("./address.txt", mode='r')
    content = address_file.readlines()

    # index error is thrown if file is empty; may have bungled this
    try:
      address = content[0]
      zipcode = content[1]
    except IndexError as indexError:
      raise ValueError('ERROR: Could not open address.txt; File empty or malformed. Please check ' + os.path.abspath("address.txt")) from indexError
  
    ch = input("Cached address detected. Do you wish to use address " + address + " and zipcode " + zipcode + "? [Y/N]: ").upper()
    if ch == "Y":
      address_file.close
    elif ch == "N":
      .addressCacheCreate()
      quit()
