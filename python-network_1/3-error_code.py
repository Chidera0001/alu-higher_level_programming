#!/usr/bin/python3
'''
A Python script that takes in a URL, sends a request to the given URL,
and displays the body of the response (decoded in utf-8).
'''
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    '''
    Fetches the response from the provided URL and displays its body.

    Usage:
    python script.py <URL>

    Parameters:
        url (str): The URL to send the HTTP request.

    Raises:
        urllib.error.HTTPError: If the server returns an HTTP error response.

    Example Output:
        The body of the HTTP response in utf-8 format.

    '''
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

