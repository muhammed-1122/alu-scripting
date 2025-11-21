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

    # IMPORTANT: allow_redirects=False is key. A 302/301 status code
    # (redirect) indicates an invalid subreddit.
    try:
        response = requests.get(
            url,
            headers=USER_AGENT,
            params=params,
            allow_redirects=False,
            timeout=5  # Add a timeout for safety
        )

        # 1. Handle invalid subreddit (redirects/not found)
        if response.status_code != 200:
            print("None")
            return

        # 2. Parse and process valid response
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
        # Handles network errors, DNS failure, connection refused, etc.
        print("None")
    except ValueError:
        # Handles potential JSON decoding errors (shouldn't happen with 200 status normally)
        print("None")


if __name__ == '__main__':
    # This block is usually for testing and shouldn't affect the check if the function is imported
    import sys
    if len(sys.argv) >= 2:
        top_ten(sys.argv[1])
