#!/usr/bin/python3
"""
Queries the Reddit API to return the number of subscribers
for a given subreddit.
"""
import requests
import sys

# Ensure headers are defined globally or within the function if preferred
USER_AGENT = {'User-Agent': 'my-python-script/0.1 by YourRedditUsername'}

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Note: allow_redirects=False is crucial for handling invalid subreddits
    response = requests.get(
        url,
        headers=USER_AGENT,
        allow_redirects=False
    )

    # Status code 200 means success.
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Navigate to the 'subscribers' key
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        except ValueError:
            # Catch JSON decode errors if response is not valid JSON
            return 0
    else:
        # Request failed (e.g., 404 Not Found, 302/301 Redirect)
        return 0

# Example of how the data structure looks for subscribers:
# response.json() -> {'data': {'subscribers': 756024, ...}, ...}
