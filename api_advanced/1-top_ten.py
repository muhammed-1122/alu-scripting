#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    # Use a unique User-Agent to avoid API rate-limiting (HTTP 429/403)
    headers = {'User-Agent': 'alx-project-advanced-api-v1.1-testing'}
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
            return

        for post in posts:
            print(post.get('data', {}).get('title'))

    except requests.exceptions.RequestException:
        print("None")
        return
    except ValueError:
        print("None")
        return
