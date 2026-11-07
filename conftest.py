import requests
import pytest


HEADER_AUTORISATION = {"Authorization": "Bearer qa-token-1"}


@pytest.fixture
def badge():
    return HEADER_AUTORISATION
