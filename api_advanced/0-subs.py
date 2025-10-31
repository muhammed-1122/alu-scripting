#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the total number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid
             or an error occurs.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Define a custom User-Agent to avoid API rate-limiting errors
    headers = {'User-Agent': 'api_advanced-project/1.0'}
    
    # Construct the URL for the subreddit's 'about' page
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        # Send the GET request, ensuring redirects are not followed
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the status code is not 200 (OK), the subreddit is invalid
        if response.status_code != 200:
            return 0

        # Parse the JSON response
        data = response.json()
        
        # Safely get the 'subscribers' count using .get()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers

    except (requests.exceptions.RequestException, ValueError):
        # Catch network errors or JSON decoding errors
        return 0
