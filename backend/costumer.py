# This class stores the users information for long term purposes.

import os
from dotenv import load_dotenv
from amadeus import Client, ResponseError

load_dotenv()

class costumer:
    def __init__(self):
        self.amadeus = Client(
            client_id= os.getenv("CLIENT_KEY"),
            client_secret= os.getenv("CLIENT_SECRET")
        )
    
