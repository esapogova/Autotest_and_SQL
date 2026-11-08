import requests
import configuration


def post_new_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body,
        timeout=30,
    )


def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track},
        timeout=30,
    )