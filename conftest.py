import pytest
import requests
import time


@pytest.fixture()
def url_search_test():
    url_search = 'https://nominatim.openstreetmap.org/search?'
    return url_search


@pytest.fixture()
def url_reverse_test():
    url_reverse = 'https://nominatim.openstreetmap.org/reverse?'
    return url_reverse
