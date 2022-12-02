import requests
import json
from TestCases import TestCases


endpoint = "<paste_your_endpoint_here>"

def random_happy_path_tests(numberOfTests):
    mytestcases = TestCases(numberOfTests) 
    numTestsPassed = 0

    for testNum, (sha_hash, password) in enumerate(mytestcases.tests.items()):
        uri = f"{endpoint}/{sha_hash}"
        print(f"Starting test number {testNum+1}.\n URI: {uri}")

        response = requests.get(uri)

        try:
            assert response.status_code == 200
        
        except:
            print(f"Failed test due to status code. Expected 200; got {response.status_code}")
            print("...")
            continue


        try:
            assert (
                json.loads(response.text).get(sha_hash) == password
                or json.loads(response.text).get(sha_hash.upper()) == password
            )

            print(f"Test {testNum+1} passes!")
            print("...")
            numTestsPassed += 1
        except:
                print(f'Failed test {testNum+1} due to response text. Expected {{"{sha_hash}": "{password}"}}')
                print(f"Got: {response.text}")
                print("...")
                print(json.loads(response.text).get(sha_hash))
            
    return numTestsPassed


x = 10
score = random_happy_path_tests(10)
if score == x:
    print("All tests pass. Yay!")
