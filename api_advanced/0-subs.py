#!/usr/bin/python3
# A function

import requests
def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {'User-Agent': 'api_advanced-project/1.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except (requests.exceptions.RequestException, ValueError):
        return 0
