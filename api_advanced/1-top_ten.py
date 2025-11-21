#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests
import sys

# Ensure headers are defined globally or within the function if preferred
USER_AGENT = {'User-Agent': 'my-python-script/0.1 by YourRedditUsername'}


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # Parameters to limit the results to the first 10
    params = {'limit': 10}
    # Note: allow_redirects=False is crucial for handling invalid subreddits
    response = requests.get(
        url,
        headers=USER_AGENT,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        try:
            data = response.json()
            # The posts are inside the 'children' list
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print("None")
                return

            # Loop through the first 10 posts and print the title
            for post in posts:
                title = post.get('data', {}).get('title')
                if title:
                    print(title)
        except ValueError:
            # Catch JSON decode errors
            print("None")
    else:
        # Request failed (e.g., 404, 302/301 Redirect)
        print("None")
