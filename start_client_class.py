import requests
import time


def send_request(url_test, valid_data):
    # пауза в 1 секунду для соблюдения правил пользования
    # https://operations.osmfoundation.org/policies/nominatim/
    time.sleep(1)
    response = requests.get(url_test)
    # проверяем есть ли элементы из списка ожидаемых данных в теле ответа
    search_results = any(
        valid_string in response.content.decode() for valid_string in valid_data)
    return search_results
