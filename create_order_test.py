import data
import sender_stand_request

# Екатерина Сапогова, 49-я когорта - Финальный проект. Инженер по тестированию плюс

def test_get_order_by_its_track():
    create_response = sender_stand_request.post_new_order(data.order_body.copy())

    assert create_response.status_code == 201, create_response.text
    track = create_response.json().get("track")
    assert track is not None

    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200, get_response.text