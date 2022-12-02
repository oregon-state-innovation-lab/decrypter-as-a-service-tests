import requests
import json

endpoint = "<paste_your_endpoint_here>"


def test_three_letter_decrypt_sha1():
    # Given
    sha_hash = "787723fb8e4dd0018273cb94157266004abe155d"

    # When
    response = requests.get(f"{endpoint}/{sha_hash}")

    # Then
    assert response.status_code == 200
    assert (
        json.loads(response.text).get(sha_hash) == "s?3"
        or json.loads(response.text).get(sha_hash.upper()) == "s?3"
    )


def test_three_letter_decrypt_sha2():
    # Given
    sha_hash = "10988de8e736c385f4326c277967d089321183b9fe3addb7b5f6aa331b60382c"

    # When
    response = requests.get(f"{endpoint}/{sha_hash}")

    # Then
    assert response.status_code == 200
    assert (
        json.loads(response.text).get(sha_hash) == "s?3"
        or json.loads(response.text).get(sha_hash.upper()) == "s?3"
    )


def test_three_letter_decrypt_invalid_sha():
    # Given
    sha_hash = "some_invalid_sha_value"

    # When
    response = requests.get(f"{endpoint}/{sha_hash}")

    # Then
    assert response.status_code == 404


test_three_letter_decrypt_sha1()
test_three_letter_decrypt_sha2()
test_three_letter_decrypt_invalid_sha()
print("All tests pass. Yay!")
