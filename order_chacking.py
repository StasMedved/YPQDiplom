import create_order
import requests
import data
import config
# Медведь Станислав, 12-я когорта — Финальный проект. Инженер по тестированию плюс
def test_getting_order_info():
    track_id = {'t': str(create_order.post_new_order(data.ORDER_BODY))}
    response = requests.get(config.URL_SERVICE + config.GET_ORDER_INFO, params=track_id)
    assert response.status_code == 200, "Expected 200 but got " + str(response.status_code)