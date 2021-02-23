#!/usr/bin/env python3

import json

import requests

from utils import update_feed


json_feed = {
    'version': 'https://jsonfeed.org/version/1.1',
    'title': 'Denver Housing Justice News',
    'home_page_url': 'https://sreynen.github.io/denver-housing-justice/',
    'feed_url': 'https://sreynen.github.io/denver-housing-justice/feed.json',
    'items': []
}

filter_keywords = ['house', 'housing', 'homeless', 'evict', 'rent']
response = requests.get('https://sreynen.github.io/denver-news/feed.json')
source_json_feed = json.loads(response.text)
for item in source_json_feed.get('items'):
    match = False
    for keyword in filter_keywords:
        if f'{keyword} ' in item.get('title', ''):
            match = True
    if match:
        json_feed['items'].append(item)
    print(item.get('id'))

update_feed('./docs/feed.json', json_feed)
