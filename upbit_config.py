import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

class UPbitConfig():

    def __init__(self):
        self.ACCESS_KEY = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
        self.SECRET_KEY = os.environ['UPBIT_OPEN_API_SECRET_KEY']
        # self.SERVER_URL = os.environ['UPBIT_OPEN_API_SERVER_URL']


upbit_config = UPbitConfig()

