import requests
import json

endpoint = input("Enter your endpoint, make sure not to add paramter: ")

def test_three_letter_decrypt_sha1():
    # Given
    sha_hash = "787723fb8e4dd0018273cb94157266004abe155d"
    myobj = {"sha_hash": sha_hash}

    # When
    response = requests.post(endpoint, json=myobj)

    # Then
    assert response.status_code == 200
    assert (
        json.loads(response.text).get(sha_hash) == "s?3"
        or json.loads(response.text).get(sha_hash.upper()) == "s?3"
    )


def test_three_letter_decrypt_sha2():
    # Given
    sha_hash = "10988de8e736c385f4326c277967d089321183b9fe3addb7b5f6aa331b60382c"
    myobj = {"sha_hash": sha_hash}

    # When
    response = requests.post(endpoint, json=myobj)

    # Then
    assert response.status_code == 200
    assert (
        json.loads(response.text).get(sha_hash) == "s?3"
        or json.loads(response.text).get(sha_hash.upper()) == "s?3"
    )


def test_three_letter_decrypt_invalid_sha():
    # Given
    myobj = {"sha_hash": "some_invalid_sha_value"}

    # When
    response = requests.post(endpoint, json=myobj)

    # Then
    assert response.status_code == 404


def test_client_sends_invalid_json():
    # Given
    myobj = {"shaHash": "c837307a9a2ad4d08ca61a4f1bd848ba3d6890fc"}

    # When
    response = requests.post(endpoint, json=myobj)

    # Then
    assert response.status_code == 400


test_three_letter_decrypt_sha1()
test_three_letter_decrypt_sha2()
test_three_letter_decrypt_invalid_sha()
test_client_sends_invalid_json()
print("All tests pass. Yay!")
