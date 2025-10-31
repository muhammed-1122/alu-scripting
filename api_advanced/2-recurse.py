#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API for all hot post titles.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list of titles (used for recursion).
        after (str): The 'after' token for pagination (used for recursion).

    Returns:
        list: A list of all titles, or None if the subreddit is invalid.
    """
    headers = {'User-Agent': 'api_advanced-project/1.0'}
    params = {
        'limit': 100,  # Request 100 posts at a time for efficiency
        'after': after
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return None  # Invalid subreddit or error

        data = response.json().get('data')
        if not data:
            return None  # No 'data' key in response

        posts = data.get('children', [])
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))

        # Get the token for the next page
        after_token = data.get('after')

        if after_token is None:
            # Base case: No more pages, return the complete list
            return hot_list
        else:
            # Recursive step: Call again with the new 'after' token
            return recurse(subreddit, hot_list, after_token)

    except (requests.exceptions.RequestException, ValueError):
        return None
