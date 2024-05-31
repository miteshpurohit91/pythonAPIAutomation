import allure
import pytest
import requests


@allure.title("Create Booking Positive")
@allure.description("TC#1 - Create Booking Positive")
@pytest.mark.crud
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-type": "application/json"}

    payload = {
        "firstname": "Jim",
        "lastname": "Wilson",
        "totalprice": 142,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2015-05-14",
            "checkout": "2019-10-27"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    print(response.headers)
    response_json = response.json()
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    print(booking_id)
    assert type(booking_id) == int
    firstname = response_json["booking"]["firstname"]
    assert firstname == "Jim2"
    checkin = response_json["booking"]["bookingdates"]["checkin"]
    assert checkin == "2015-05-14"

    # Response Body verification
    # Headers
    # Status Code
    # JSON Schema Validation
    # Time Response

@allure.title("Create Booking Negative")
@allure.description("TC#2 Verify that the booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-type" : "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    #Assertion
    assert response.status_code == 500

