# Structure of the MQS

When __main__.py is first run by invocation of `python3 mqs` the follow sequence occurs:  
  
- The coordLookup function from the lookup module is invoked, and it asks for a street address and zip code. It uses this information to query the US Census Bureau's API and returns coordinates if successful.

- These are immediately passed into the next function, also in the lookup module. This function is the officeLookup module. It uses the coordinates to query the NWS API to check what forecasting office is responsible for the coordinates given. The designation it looks for is a three-letter code.

- Once this code is found, it and the coordinates are passed to the main module, which queries the NWS forecasting API to fetch weather information.
