#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit. Prints None if the subreddit is invalid.
"""
import requests

# Set a custom User-Agent
USER_AGENT = {'User-Agent': 'my-python-script/0.1 by YourRedditUsername'}


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Parameters to limit the results to the first 10
    params = {'limit': 10}

    try:
        response = requests.get(
            url,
            headers=USER_AGENT,
            params=params,
            allow_redirects=False,
            timeout=5
        )

        # Handle invalid subreddit (redirects/not found)
        if response.status_code != 200:
            print("None")
            return

        # Parse and process valid response
        data = response.json()

        # Navigate the nested JSON structure
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        # Print the titles
        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except requests.exceptions.RequestException:
        # Handles network errors
        print("None")
    except ValueError:
        # Handles JSON decoding errors
        print("None")
