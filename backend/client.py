# This class stores the users information for long term purposes.
import os
from dotenv import load_dotenv
from amadeus import Client, ResponseError
import requests

load_dotenv()


class Client:
    def __init__(self):
        self.client_id = os.getenv("CLIENT_KEY"),
        self.client_secret = os.getenv("CLIENT_SECRET")

    

# Code below works, sad that SDK didnt work
    def generateAccessToken(self):
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
            self.access_token = data.get('access_token')
            return self.access_token
        else:
            print("Error:", response.status_code, response.text)
            return None



    def getFlightOffersSearch(origin, destination, date, adults, max_results):
        
        # generate token whenever needed
        if not self.access_token:
            self.generateAccessToken()

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
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
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
                return flight_details
                # for i, flight in enumerate(flight_details, start=0):
                #     print(f"\nOption {i}:")
                #     print(json.dumps(flight, indent=2))
        except ResponseError as error:
            print("Status Code:", error.response.status_code)
            print("Error Body:", error.response.body)


# class client:
#     def __init__(self):
#         self.amadeus = Client(
#             client_id= os.getenv("CLIENT_KEY"),
#             client_secret= os.getenv("CLIENT_SECRET")
#         )
#     def search_flights(self, origin, destination, departure_date, adults = 1, max_results = 7):
#         try:
#             response = self.amadeus.shopping.flight_offers_search.get(
#                 originLocationCode = origin,
#                 destinationLocationCode = destination,
#                 departureDate = departure_date,
#                 adults = adults
#             )
#             return response.data
#         except ResponseError as error:
#             print(error.code)
#             print(error.response)

