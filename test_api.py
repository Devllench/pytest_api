import pytest
from data_class import ValidAssertClass
from start_client_class import send_request


class TestApiClass:

    @pytest.mark.parametrize("format_test", ['&format=xml', '&format=json',
                                             '&format=jsonv2', '&format=geojson', '&format=geocodejson'])
    @pytest.mark.parametrize("query_test", ['q=dybenko+street', 'q=metro+nevskie+prospekt'])
    @pytest.mark.parametrize("url_test", ['https://nominatim.openstreetmap.org/search?'])
    def test_search(self, url_test, query_test, format_test):
        assert send_request(url_test + query_test + format_test, ValidAssertClass.valid_coordinates)

    @pytest.mark.parametrize("format_test", ['&format=xml', '&format=json',
                                             '&format=jsonv2', '&format=geojson', '&format=geocodejson'])
    @pytest.mark.parametrize("coordinates_test", ['lat=59.94080&lon=30.45652', 'lat=60.23105&lon=25.03549'])
    @pytest.mark.parametrize("url_test", ['https://nominatim.openstreetmap.org/reverse?'])
    def test_reverse(self, url_test, coordinates_test, format_test):
        assert send_request(url_test + coordinates_test + format_test, ValidAssertClass.valid_address)

    @pytest.mark.parametrize("addr_det", ['&addressdetails=1'])
    @pytest.mark.parametrize("format_test", ['&format=xml'])
    @pytest.mark.parametrize("coordinates_test", ['q=dybenko+street'])
    @pytest.mark.parametrize("url_test", ['https://nominatim.openstreetmap.org/search?'])
    def test_add_details(self, url_test, coordinates_test, format_test, addr_det):
        assert send_request(url_test + coordinates_test + format_test + addr_det, ValidAssertClass.valid_coordinates)
