# This file is the main backend funcitonality that will call the API
import os
from dotenv import load_dotenv
from amadeus import Client, Location, ResponseError
import requests
import json
# GET: retrieving data
# POST: sending data

load_dotenv()

# Goal: get cheapest total international travel cost

# after flight search, must use flight offers price to confirm price
'''
User input: Origin, destitantion, number of people, date range (will show multiple days if needed)
User input optional: prefered airlines, baggage quantity 
'''

#response.data is a Reasource object, not dictionary.
amadeus = Client(
    client_id= os.getenv("CLIENT_KEY"),
    client_secret= os.getenv("CLIENT_SECRET"),
    hostname='test'
)

'''origin = input("Origin: ")
destination = input("Final Destination: ")
date = input("Departure date (YYYY-MM-DD): " )
date = date.strip()
adults = int(input("Number of adults: ").strip())
max = int(input("Max number of flight options: ").strip())'''

origin = "JFK"
destination = "LHR"
date = "2025-12-10"
adults = 1

def getFlightOfferSearch(origin, destination, adults, max_results = 2, currency = "USD"):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=adults,
            currencyCode=currency,
            max=max_results
        )
        
        # response.data is a list of dicts (not JSON string)
        print("Here are some flight options: \n")
        print(response.data)
    except ResponseError as error:
        print("Error:", error)

getFlightOfferSearch()


# YAY
# API each flight: price, fare details, airlines names, baggage allowances, departure terminals
# Unable to print because flight details is too complex to print in terminal. I believe this is the case because it is a list of dictionaries.
# /v2/shopping/flight-offers → amadeus.shopping.flight_offers_search.get()
# Access token so far? I'm so confused what this all means: 2cRYqWZnxPKBDWTE52hrBU8ZVt20

# Goal: User types origin, destination, date, persons traveling, roundtrip or oneway, engine shows options.
# shows flights, luggage allowed (must see how to find this), total travel time, price, add to cart

# Create a whatsapp / IG extension so that users can see flight options on chat, user friendly and super accessible on the go.