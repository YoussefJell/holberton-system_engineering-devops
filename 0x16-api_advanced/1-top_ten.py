#!/usr/bin/python3
"""1-top_ten Module"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of
        the first 10 hot posts listed for a given subreddit."""
    if not subreddit:
        print('None')
    url = "https://www.reddit.com"
    endpoint = f"/r/{subreddit}/hot.json?limit=10"
    request = requests.get(f"{url}{endpoint}", headers={
        'User-agent': 'Mozilla/5.0'}, allow_redirects=False)
    if request.status_code == 200:
        for elem in request.json().get('data').get('children'):
            if elem.get('data').get('title'):
                print(elem.get('data').get('title'))
    else:
        print('None')
