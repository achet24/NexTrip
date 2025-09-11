# This file is the main backend funcitonality that will call the API
import os
from dotenv import load_dotenv
from amadeus import Client, Location, ResponseError
# GET: retrieving data
# POST: sending data
load_dotenv()
# Goal: get cheapest total international travel cost

'''
User input: Origin, destitantion, number of people, date range (will show multiple days if needed)
User input optional: prefered airlines, baggage quantity 

'''

amadeus = Client(
    client_id= os.getenv("CLIENT_KEY"),
    client_secret= os.getenv("CLIENT_SECRET")
)

origin = input("Origin: ")
destination = input("Final Destination: ")
date = input("Departure date (YYY-MM-DD)" )
date = date.strip()
adults = input("Number of adults: ")
max = input("Max number of flight options: ")
max = max.strip()



try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode=origin,
        destinationLocationCode=destination,
        departureDate=date,
        adults=adults,
        max=max
    )    
    print(response.data)
except ResponseError as error:
    print(error)


# /v2/shopping/flight-offers → amadeus.shopping.flight_offers_search.get()
# Access token so far? I'm so confused what this all means: 2cRYqWZnxPKBDWTE52hrBU8ZVt20
