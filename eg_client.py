import requests
import json


def send_event(url, api_token, title):
    """Send an event to the event girl with the given url, the api_token and
    the title and return the result of the request.

    Parameters:
        url - the url of your eventgirl instance.
        api_token - the token you received.
        title - the actual title of the event.
    """
    payload = {
        "title": title,
        "api_token": api_token
    }
    headers = {'content-type': 'application/json'}
    ret = requests.post(url, data=json.dumps(payload), headers=headers)

    return ret
