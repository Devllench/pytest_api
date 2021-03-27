import pytest, requests


class TestApiClass:

    #@pytest.mark.parametrize("data_test", ['login'])
    #@pytest.mark.parametrize("valid_assert", ['abc'])
    def test_search(self):
        response = requests.get("https://nominatim.openstreetmap.org/search?q=dybenko+street&format=xml")
        assert response.status_code == 220

    def test_reverse(self):
        response = requests.get("https://nominatim.openstreetmap.org/reverse?format=xml&lat=52.5487429714954&lon=-1.81602098644987")
        assert response.status_code == 200
