import requests
import data
import  configuration
import  sender_stand

def get_status_order():
    return requests.get(configuration.URL_SERVISE + configuration.GET_ORDER,
                         params = {'t' : sender_stand.get_order_track()},
                         headers = data.headers)


def  test_positiv():
    responce =get_status_order()
    assert  responce.status_code == 200