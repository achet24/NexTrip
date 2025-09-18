import os
from amadeus import Client, Location, ResponseError
from dotenv import load_dotenv
import requests


load_dotenv()

amadeus = Client(
    client_id = os.getenv("CLIENT_KEY"),
    client_secret = os.getenv("CLIENT_SECRET")

)

# Code below works, sad that SDK didnt work
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

    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=adults,
            max=max_results
        )
        flight_details = response.data  # fixed typo
        if not flight_details:
            print("No flights found for the given criteria.")
        else:
            print("Here are some flight options:")
            print(flight_details)
            # for i, flight in enumerate(flight_details, start=0):
            #     print(f"\nOption {i}:")
            #     print(json.dumps(flight, indent=2))
    except ResponseError as error:
        print("Status Code:", error.response.status_code)
        print("Error Body:", error.response.body)

origin = "JFK"
destination = "LHR"
date = "2025-12-10"
adults = 1
max_results = 5

getFlightOffersSearch(origin, destination, date, adults, max_results)

# Giving this a break, today I will work on front-end.






#From amadeus SDK. The SDK for the test environment atleast, 
# try:
#     response = amadeus.shopping.flight_offers_search.get(
#         originLocationCode="JFK",
#         destinationLocationCode="LHR",
#         departureDate="2025-12-10",
#         adults=1,
#         currencyCode="USD",
#         max=5
#     )
#     print("Here are some flight options: \n")
#     print(response.data)
# except ResponseError as error:
#     print("Error:", error.code, error.response)

# try:
#     response = amadeus.reference_data.locations.get(
#         keyword='LON',
#         subType=Location.AIRPORT
#     )    
#     print(response.body)
# except ResponseError as error:
#     print(error.code)