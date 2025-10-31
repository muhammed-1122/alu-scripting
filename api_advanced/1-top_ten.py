#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    headers = {'User-Agent': 'api_advanced-project/1.0'}
    params = {'limit': 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            print("None")
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("None")  # Subreddit is valid but has no posts
            return

        for post in posts:
            print(post.get('data', {}).get('title'))

    except (requests.exceptions.RequestException, ValueError):
        print("None")
