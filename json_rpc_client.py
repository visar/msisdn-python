import json

import requests


def main():
    url = "http://localhost:9000/jsonrpc"
    headers = {'content-type': 'application/json'}

    payload = {
        "method": "parser.transform",
        "params": ["+38976123456"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(response)

    assert response["result"]["mno_identifier"] == "VIP Operator"
    assert response["result"]["country_dialing_code"] == "389"
    assert response["result"]["country_identifier"] == "MK"
    assert response["jsonrpc"] == "2.0"
    assert response["id"] == 0

    payload = {
        "method": "parser.transform",
        "params": ["a"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(response)

    assert response["error"]["data"]["message"] == "Input parameter must be integer"
    assert response["error"]["code"] == -32000
    assert response["jsonrpc"] == "2.0"
    assert response["id"] == 0

    payload = {
        "method": "parser.transform",
        "params": ["+3897611111111111"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(response)

    assert response["error"]["data"]["message"] == "Input should be 15 digits at most"
    assert response["error"]["code"] == -32000
    assert response["jsonrpc"] == "2.0"
    assert response["id"] == 0

    payload = {
        "method": "parser.transform",
        "params": ["+389"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(response)

    assert response["error"]["data"]["message"] == "Invalid number"
    assert response["error"]["code"] == -32000
    assert response["jsonrpc"] == "2.0"
    assert response["id"] == 0


if __name__ == "__main__":
    main()
