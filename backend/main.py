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

# response.data is a Reasource object, not dictionary.
# amadeus = Client(
#     client_id= os.getenv("CLIENT_KEY"),
#     client_secret= os.getenv("CLIENT_SECRET"),
#     hostname='test'
# )

def generateAccessToken():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_KEY"),
        "client_secret": os.getenv("CLIENT_SECRET")
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        access_token = data.get('access_token')
        return access_token
    else:
        print("Error:", response.status_code, response.text)

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
max_results = 2

def getFlightOffersSearch(origin, destination, date, adults, max_results):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    payload = {
        "currencyCode": "USD",
        "originDestinations": [
            {
                "id": "1",
                "originLocationCode": origin,
                "destinationLocationCode": destination,
                "departureDateTimeRange": {
                    "date": date
                }
            }
        ],
        "travelers": [
            {
                "id": "1",
                "travelerType": "ADULT"
            }
        ],
        "sources": ["GDS"],
        "searchCriteria": {
            "maxFlightOffers": max_results
        }
    }
    headers = {
        "Content-Type": "application/vnd.amadeus+json",
        "Authorization": "Bearer " + generateAccessToken()
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error:", response.status_code, response.text)

    # try:
    #     response = amadeus.shopping.flight_offers_search.get(
    #         originLocationCode=origin,
    #         destinationLocationCode=destination,
    #         departureDate=date,
    #         adults=adults,
    #         max=max_results
    #     )
    #     flight_details = response.data  # fixed typo
    #     if not flight_details:
    #         print("No flights found for the given criteria.")
    #     else:
    #         print("Here are some flight options:")
    #         for i, flight in enumerate(flight_details, start=0):
    #             print(f"\nOption {i}:")
    #             print(json.dumps(flight, indent=2))
    # except ResponseError as error:
    #     print("Status Code:", error.response.status_code)
    #     print("Error Body:", error.response.body)

getFlightOffersSearch(origin, destination, date, adults, max_results)

# YAY
# API each flight: price, fare details, airlines names, baggage allowances, departure terminals
# Unable to print because flight details is too complex to print in terminal. I believe this is the case because it is a list of dictionaries.
# /v2/shopping/flight-offers → amadeus.shopping.flight_offers_search.get()
# Access token so far? I'm so confused what this all means: 2cRYqWZnxPKBDWTE52hrBU8ZVt20

# Goal: User types origin, destination, date, persons traveling, roundtrip or oneway, engine shows options.
# shows flights, luggage allowed (must see how to find this), total travel time, price, add to cart

# Create a whatsapp / IG extension so that users can see flight options on chat, user friendly and super accessible on the go.