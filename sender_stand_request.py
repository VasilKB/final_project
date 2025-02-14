import requests
import data
import  configuration
def create_order(body):
    return requests.post(configuration.URL_SERVISE + configuration.NEW_ORDER,
                         json=body,
                         headers=data.headers)

def get_status_order(track):
    return requests.get(configuration.URL_SERVISE + configuration.GET_ORDER,
                        params={'t': track},
                        headers=data.headers)
