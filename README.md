# CrackStationWrapper

A test harness for the `Decrypter as a Service` assignment in CS 561.

## Usage

This will be updated to be more meaningful when the TA has more time. Pull requests are welcome :) 

For now: 

- you need python3 for this to work 
- git clone the repo
- cd into it and do `pip3 install -r requirements.txt`
- choose either `api_test_get.py` or `api_test_post.py` depending on how you have implemented your endpoint
- Enter your endpoint: (example: `endpoint = "https://5xduexoja5.execute-api.us-east-1.amazonaws.com/password"`)

- To run : `python3 api_test_get.py`

If you need to debug either use a Debugger or print `reponse.status_code` and `response.text` where it makes sense :) 
