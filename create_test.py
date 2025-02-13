import requests
import data
import  configuration
# Василиса Касьянова-Безниско, 26-я когорта — Финальный проект. Инженер по тестированию плюс
def  test_positiv():
    def create_order(body):
        return requests.post(configuration.URL_SERVISE + configuration.NEW_ORDER,
                             json=body,
                             headers=data.headers)

    track = create_order(data.body).json()['track']
    get_status_order = requests.get(configuration.URL_SERVISE + configuration.GET_ORDER,
                        params={'t': track},
                        headers=data.headers)
    assert  get_status_order.status_code == 200