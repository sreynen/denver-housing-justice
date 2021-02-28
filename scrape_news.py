#!/usr/bin/env python3

import json
import re

import requests

from utils import update_feed


json_feed = {
    'version': 'https://jsonfeed.org/version/1.1',
    'title': 'Denver Housing Justice News',
    'home_page_url': 'https://sreynen.github.io/denver-housing-justice/',
    'feed_url': 'https://sreynen.github.io/denver-housing-justice/feed.json',
    'items': []
}

filter_key_phrases = [
    'house prices', 'housing',
    'homeless', 'homelessness',
    'evict', 'eviction',
    'rent',
    'property tax', 'property taxes',
]
response = requests.get('https://sreynen.github.io/denver-news/feed.json')
source_json_feed = json.loads(response.text)
for item in source_json_feed.get('items'):
    match = False
    title_words = re.findall(r"[\w']+", item.get('title', ''))
    title_substring = ' '.join([word.lower() for word in title_words]).lower()
    title_string = f" {title_substring} "
    for phrase in filter_key_phrases:
        phrase_string = f" {phrase} "
        if phrase_string in title_string:
            match = True
    if match:
        json_feed['items'].append(item)

update_feed('./docs/feed.json', json_feed)
