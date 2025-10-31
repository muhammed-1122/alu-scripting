#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None,
                lower_word_list=None):
    """
    Recursively counts keywords in hot post titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): The list of keywords to count.
        after (str): The 'after' token for pagination.
        counts (dict): A dictionary accumulating keyword counts.
        lower_word_list (list): Normalized list of keywords for multipliers.
    """

    # Initialize on the first call
    if counts is None:
        # Create a list of all keywords in lowercase
        lower_word_list = [word.lower() for word in word_list]
        # Create a counts dict with all unique lowercase keywords
        counts = {}
        for word in lower_word_list:
            counts[word] = 0

    headers = {'User-Agent': 'api_advanced-project/1.0'}
    params = {'limit': 100, 'after': after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return  # Invalid subreddit or error, print nothing

        data = response.json().get('data')
        if not data:
            return

        posts = data.get('children', [])
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            title_words = title.split()
            # Increment count for each occurrence in the title
            for t_word in title_words:
                if t_word in counts:
                    counts[t_word] += 1

        after_token = data.get('after')

        if after_token is None:
            # Base case: All pages processed, print results
            print_counts = {}
            # Apply multipliers from the original word_list
            for word in set(lower_word_list):
                multiplier = lower_word_list.count(word)
                total = counts[word] * multiplier
                if total > 0:
                    print_counts[word] = total

            if not print_counts:
                return  # No matches found

            # Sort: by count (desc), then alphabetically (asc)
            sorted_items = sorted(print_counts.items(),
                                  key=lambda item: (-item[1], item[0]))

            for word, count in sorted_items:
                print("{}: {}".format(word, count))

            return  # End recursion

        else:
            # Recursive step
            count_words(subreddit, word_list, after_token, counts,
                        lower_word_list)

    except (requests.exceptions.RequestException, ValueError):
        return  # Fail silently and print nothing
