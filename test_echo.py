import requests
import pytest

URL = "https://postman-echo.com"

URL_BEARER = "https://httpbin.org"

HEADER_AUTORISATION = {"Authorization": "Bearer qa-token-1"}


def test_get_echo_200():
    requete = requests.get(f"{URL}/get")
    assert requete.status_code == 999
    assert requete.json()["url"] == f"{URL}/get"


def test_get_status_without_bearer():
    assert requests.get(f"{URL_BEARER}/bearer").status_code == 401


def test_get_status_with_token(badge):

    requete = requests.get(f"{URL_BEARER}/bearer", headers=badge)
    assert requete.status_code == 200
    assert requete.json()["authenticated"] == True


@pytest.mark.parametrize("param,attendu", [("A101", 200), ("B202", 200)])
def test_get_status_salles_available(param, attendu):
    requete = requests.get(f"{URL}/get?salle={param}")
    assert requete.status_code == attendu
    assert requete.json()["args"]["salle"] == param


def test_create_salle():
    create = requests.post(f"{URL}/post", json={"salle": "A101"})
    assert create.status_code == 200
    assert create.json()["json"]["salle"] == "A101"


def test_put_body_salle():
    change = requests.put(f"{URL}/put", json={"salle": "B202"})
    assert change.status_code == 200
    assert change.json()["json"]["salle"] == "B202"


def test_patch_body_salle():
    change = requests.patch(f"{URL}/patch", json={"salle": "C303"})
    assert change.status_code == 200
    assert change.json()["json"]["salle"] == "C303"


def test_delete_echo():
    delete = requests.delete(f"{URL}/delete")
    assert delete.status_code == 200
