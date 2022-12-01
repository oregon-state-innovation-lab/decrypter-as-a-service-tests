import requests

endpoint = "https://32a86dzdsa.execute-api.us-east-1.amazonaws.com/v1/password"
request_type = "POST"

if request_type == "GET":
    # GET endpoint

    # Happy path
    # sha_hash key is present
    response = requests.get(
        f"{endpoint}/10988de8e736c385f4326c277967d089321183b9fe3addb7b5f6aa331b60382c"
    )

    assert response.status_code == 200
    assert (
        response.text
        == '{"10988de8e736c385f4326c277967d089321183b9fe3addb7b5f6aa331b60382c": "s?3"}'
    )

    # Rainy day
    # sha_hash key not present
    response = requests.get(
        f"{endpoint}10988de8e736c385f4326c277967d089321183b9fe3addb7b5f6aa331b603"
    )

    assert response.status_code == 404
else:
    # POST endpoint
    url = "https://ruo323g6yh.execute-api.us-east-1.amazonaws.com/prod/decrypt"

    # Happy path
    myobj = {"sha_hash": "c837307a9a2ad4d08ca61a4f1bd848ba3d6890fc"}
    response = requests.post(url, json=myobj)
    assert response.status_code == 200
    assert (
        response.text
        == '{"10988de8e736c385f4326c277967d089321183b9fe3addb7b5f6aa331b60382c": "s?3"}'
    )

    # Rainy day

    # client sends invalid JSON
    myobj = {"shaHash": "c837307a9a2ad4d08ca61a4f1bd848ba3d6890fc"}
    response = requests.post(url, json=myobj)

    assert response.status_code == 400

    # sha_hash key not present
    myobj = {"sha_hash": "some_random_value"}
    response = requests.post(url, json=myobj)

    assert response.status_code == 404
