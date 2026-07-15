#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/example)"
    }

    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print("None")
            return

        posts = response.json()["data"]["children"]

        for post in posts:
            print(post["data"]["title"])

    except requests.RequestException:
        print("None")
