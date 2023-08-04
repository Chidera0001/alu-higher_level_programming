#!/usr/bin/python3
'''
A Python script that fetches https://alx-intranet.hbtn.io/status
'''
import requests

if __name__ == "__main__":
    '''
    Fetches the status information from https://alx-intranet.hbtn.io/status and prints the response.

    Example Output:
        Body response:
            - type: <class 'str'>
            - content: {"status": "OK"}
    '''
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(response.text)}\n\t- content: {response.text}")

