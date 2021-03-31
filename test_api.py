import pytest
from start_client_class import send_request, get_test_data


class TestApiClass:

    @pytest.mark.parametrize("format_test", ['&format=xml', '&format=json',
                                             '&format=jsonv2', '&format=geojson', '&format=geocodejson'])
    @pytest.mark.parametrize("query_test", ['q=metro+nevskie+prospekt'])
    def test_format_search(self, url_search_test, query_test, format_test):
        body = send_request(url_search_test + query_test + format_test)
        if format_test in ['&format=xml']:
            test_data = get_test_data(body, "lat='", ' display_name')
            assert test_data == "lat='59.9351318' lon='30.3294301'"
        elif format_test in ['&format=json', '&format=jsonv2']:
            test_data = get_test_data(body, '"lat":', ',"display_name"')
            assert test_data == '"lat":"59.9351318","lon":"30.3294301"'
        elif format_test in ['&format=geojson', '&format=geocodejson']:
            test_data = get_test_data(body, 'coordinates":[', ']}}]}')
            assert test_data == 'coordinates":[30.3294301,59.9351318'

    @pytest.mark.parametrize("format_test", ['&format=xml', '&format=json',
                                             '&format=jsonv2', '&format=geojson', '&format=geocodejson'])
    @pytest.mark.parametrize("coordinates_test", ['lat=59.94080&lon=30.45652'])
    def test_format_reverse(self, url_reverse_test, coordinates_test, format_test):
        body = send_request(url_reverse_test + coordinates_test + format_test)
        if format_test in ['&format=xml']:
            test_data = get_test_data(body, "address_rank='30'>", '</result')
            assert test_data == "address_rank='30'>Metro, 4 литА, проспект Косыгина, округ Пороховые, Санкт-Петербург, Северо-Западный федеральный округ, 195279, Россия"
        elif format_test in ['&format=json', '&format=jsonv2', '&format=geojson']:
            test_data = get_test_data(body, '"display_name":"', '","address"')
            assert test_data == '"display_name":"Metro, 4 литА, проспект Косыгина, округ Пороховые, Санкт-Петербург, Северо-Западный федеральный округ, 195279, Россия'
        elif format_test in ['&format=geocodejson']:
            test_data = get_test_data(body, '"label":', '","name"')
            assert test_data == '"label":"Metro, 4 литА, проспект Косыгина, округ Пороховые, Санкт-Петербург, Северо-Западный федеральный округ, 195279, Россия'


    # @pytest.mark.parametrize("addr_det", ['&addressdetails=1'])
    # @pytest.mark.parametrize("format_test", ['&format=xml'])
    # @pytest.mark.parametrize("coordinates_test", ['q=dybenko+street'])
    # @pytest.mark.parametrize("url_test", ['https://nominatim.openstreetmap.org/search?'])
    # def test_add_details(self, url_test, coordinates_test, format_test, addr_det):

