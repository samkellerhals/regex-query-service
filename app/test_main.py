import requests
import pytest


def test_get():

    response = requests.get("http://0.0.0.0:80/api/v1/regex/get-queries")

    assert response.status_code == 200


def test_post():

    body = {
        "column_name": "name",
        "search_word": "Pepsi",
        "query": "default",
        "save": False
    }

    response = requests.post("http://0.0.0.0:80/api/v1/regex/add-query", json=body)

    assert response.status_code == 201


def test_put():

    update = {
      "regex_query": "string",
      "search_word": "string",
      "num_outlets": 0,
      "per_outlets": 0,
      "brand_id": [
        "string"
      ]
    }

    # update this record
    response = requests.put("http://0.0.0.0:80/api/v1/regex/5", json=update)

    assert response.status_code == 200
