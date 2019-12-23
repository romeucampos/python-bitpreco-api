import json
import requests

from .erros import ApiError


class Api:   
    def __init__(self, api_key='', signature=''):
        self.url = 'https://api.bitpreco.com/btc-brl/'
        self.host = 'https://api.bitpreco.com/trading/'
        self.headers = {'Content-type': 'application/json'}
        self.keys = signature + api_key

    def __check_response_public(self, response):
        try:
            rsp =  response.json()
        except:
            response.raise_for_status()
            raise ApiError('Error parsing json')
        return rsp

    def __check_response_private(self, response):
        try:
            rsp =  response.json()
        except:
            response.raise_for_status()
            raise ApiError('Error parsing json')
        
        if 'success' in rsp and not rsp['success']:
            raise ApiError(f"Invalid response: {rsp['message_cod']}") 
        return rsp
     
    def __get(self, data):
        response = requests.get(self.url + data)
        return self.__check_response_public(response)
        
    def __post(self, data):
        response = requests.post(self.host, data=json.dumps(data), headers=self.headers)
        return self.__check_response_private(response)

    def ticker(self):
        return self.__get('ticker')

    def orderbook(self):
        return self.__get('orderbook')

    def trades(self):
        return self.__get('trades')

    def exchanges(self):
        return self.__get('exchanges')
        
    def balance(self):
        return self.__post({"cmd": "balance","auth_token": self.keys})

    def open_orders(self):
        return self.__post({"cmd": "open_orders", "auth_token": self.keys})

    def buy(self, price, amount):
        return self.__post({"cmd":"buy", "market":"BTC-BRL", "price": price, "amount": amount, "auth_token": self.keys})

    def sell(self, price, amount):
        return self.__post({"cmd":"sell", "market":"BTC-BRL", "price": price, "amount": amount, "auth_token": self.keys})

    def order_cancel(self, order_id):
        return self.__post({"cmd":"order_cancel", "order_id": order_id, "auth_token": self.keys})

    def all_orders_cancel(self):
        return self.__post({"cmd": "all_orders_cancel", "auth_token": self.keys})

    def order_status(self, order_id):
        return self.__post({"cmd":"order_status", "order_id": order_id, "auth_token": self.keys})
    