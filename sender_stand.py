import data
import  configuration
import requests

def create_order(body):
    return requests.post(configuration.URL_SERVISE + configuration.NEW_ORDER,
                         json = body,
                         headers = data.headers)

def get_order_track():
    create_order(data.body)
    track =create_order(data.body).json()['track']
    return track

