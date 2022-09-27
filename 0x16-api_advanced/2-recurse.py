#!/usr/bin/python3
"""1-2-recurse Module"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    if not subreddit:
        return None
    url = "https://www.reddit.com"
    endpoint = f"/r/{subreddit}/hot.json?after={after}"

    request = requests.get(f"{url}{endpoint}",
                           headers={'User-agent': 'Mozilla/5.0'},
                           allow_redirects=False)

    if request.status_code == 200:
        children = request.json().get('data').get('children')
        after = request.json().get('data').get('after')

        for elem in children:
            hot_list.append(elem.get('data').get('title'))

        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list

    return None
