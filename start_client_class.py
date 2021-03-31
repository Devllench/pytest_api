import requests
import time


def send_request(url_test):
    # пауза в 1 секунду для соблюдения правил пользования
    # https://operations.osmfoundation.org/policies/nominatim/
    time.sleep(1)
    response = requests.get(url_test)
    if response.status_code == 200:
        return response.content.decode()
    elif response.status_code == 200:
        print("502, a lot of request")


def get_test_data(body, left_border, right_border):
    data = body[body.find(left_border):body.find(right_border)]
    return data
