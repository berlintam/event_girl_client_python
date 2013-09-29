import requests
import json


def send_event(url, api_token, title):
    """Send an event to the event girl with the given url, the api_token and
    the title and return the result of the request.

    :param url: the url of your eventgirl instance.
    :param api_token: the token you received.
    :param title: the actual title of the event.

    Usage::

        >>> import eventgirl
        >>> eventgirl.send_event(
                url="http://yoururl.com/incoming_events.json",
                api_token="your_api_token",
                title="Your Title"
            )
    """
    payload = {
        "title": title,
        "api_token": api_token
    }
    headers = {'content-type': 'application/json'}
    ret = requests.post(url, data=json.dumps(payload), headers=headers)
    return ret
