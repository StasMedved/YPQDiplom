import requests
import config
import data


def post_new_order(body):
    response = requests.post(config.URL_SERVICE + config.CREATE_ORDER_URL, json=body, headers=data.HEADERS)
    return response.json()["track"]