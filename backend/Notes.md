 Main Previous code attempts:
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
#         print("Error:", response.status_code, response.text)



# def getFlightOffersSearch(origin, destination, date, adults, max_results):
#     url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
#     payload = {
#         "currencyCode": "USD",
#         "originDestinations": [
#             {
#                 "id": "1",
#                 "originLocationCode": origin,
#                 "destinationLocationCode": destination,
#                 "departureDateTimeRange": {
#                     "date": date
#                 }
#             }
#         ],
#         "travelers": [
#             {
#                 "id": "1",
#                 "travelerType": "ADULT"
#             }
#         ],
#         "sources": ["GDS"],
#         "searchCriteria": {
#             "maxFlightOffers": max_results
#         }
#     }
#     headers = {
#         "Content-Type": "application/vnd.amadeus+json",
#         "Authorization": "Bearer " + generateAccessToken()
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print("Error:", response.status_code, response.text)

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

# getFlightOffersSearch(origin, destination, date, adults, max_results)