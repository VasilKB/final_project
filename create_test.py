import requests
import data
import  configuration
import sender_stand_request


# Василиса Касьянова-Безниско, 26-я когорта — Финальный проект. Инженер по тестированию плюс
def  test_positiv():
    track = sender_stand_request.create_order(data.body).json()['track']
    get_status = sender_stand_request.get_status_order(track)
    assert get_status.status_code == 200