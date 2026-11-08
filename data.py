from datetime import date, timedelta

order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": (date.today() + timedelta(days=3)).isoformat(),
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ],
}