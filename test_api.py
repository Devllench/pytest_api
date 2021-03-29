import pytest
import requests
import time

from date_class import ValidAssertClass


class TestApiClass:

    @pytest.mark.parametrize("format_test", ['format=xml', 'format=json',
                                             'format=jsonv2', 'format=geojson', 'format=geocodejson'])
    @pytest.mark.parametrize("query_test", ['q=dybenko+street', 'q=metro+nevskie+prospekt'])
    @pytest.mark.parametrize("url_test", ['https://nominatim.openstreetmap.org/search?'])
    def test_search(self, url_test, query_test, format_test):
        # пауза в 1 секунду для соблюдения правил пользования
        # https://operations.osmfoundation.org/policies/nominatim/
        time.sleep(1)
        response = requests.get(url_test + query_test + '&' + format_test)
        # проверяем есть ли элементы из списка ожидаемых данных в теле ответа
        assert any(valid_string in response.content.decode() for valid_string in ValidAssertClass.valid_coordinates)

    @pytest.mark.parametrize("format_test", ['format=xml', 'format=json',
                                             'format=jsonv2', 'format=geojson', 'format=geocodejson'])
    @pytest.mark.parametrize("coordinates_test", ['lat=59.94080&lon=30.45652','lat=60.23105&lon=25.03549'])
    @pytest.mark.parametrize("url_test", ['https://nominatim.openstreetmap.org/reverse?'])
    def test_reverse(self, url_test, coordinates_test, format_test):
        # пауза в 1 секунду для соблюдения правил пользования
        # https://operations.osmfoundation.org/policies/nominatim/
        time.sleep(1)
        response = requests.get(url_test + coordinates_test + '&' + format_test)
        # проверяем есть ли элементы из списка ожидаемых данных в теле ответа
        assert any(valid_string in response.content.decode() for valid_string in ValidAssertClass.valid_address)
