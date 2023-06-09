import requests


def test_favourite_languages() -> None:
    rs = requests.get(
        "http://localhost:8000/api/v1/favourite_languages", timeout=10
    )
    assert rs.json() == {
        "jen": "python",
        "sarah": "c",
        "edward": "ruby",
        "phil": "python",
    }
