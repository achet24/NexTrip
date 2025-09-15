# This class stores the users information for long term purposes.
import os
from dotenv import load_dotenv
from amadeus import Client, ResponseError

load_dotenv()

class client:
    def __init__(self):
        self.amadeus = Client(
            client_id= os.getenv("CLIENT_KEY"),
            client_secret= os.getenv("CLIENT_SECRET")
        )
    xs
    def search_flights(self, origin, destination, departure_date, adults = 1, max_results = 7):
        try:
            response = self.amadeus.shopping.flight_offers_search.get(
                originLocationCode = origin,
                destinationLocationCode = destination,
                departureDate = departure_date,
                adults = adults
            )
            return response.data
        except ResponseError as error:
            print(error)
#return {"error": str(error)}

