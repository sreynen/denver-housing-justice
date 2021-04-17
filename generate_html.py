#!/usr/bin/env python3

import json
from os import listdir, path

import yaml


with open('./docs/feed.json', 'r', encoding='utf8') as file:
  news = json.load(file)

with open('./templates/index.html', 'r', encoding='utf8') as file:
  html_template = file.read()

with open('./templates/list.html', 'r', encoding='utf8') as file:
  list_template = file.read()

with open('./templates/list-news-item.html', 'r', encoding='utf8') as file:
  news_item_template = file.read()

news_list_items = [news_item_template
                   .replace('{{ url }}', item.get('url'))
                   .replace('{{ title }}', item.get('title'))
                   for item in news.get('items', [])]
news_list = list_template.replace('{{ items }}',
                                  ''.join(news_list_items))

advocates = []
for filepath in listdir('./data/advocates/'):
    fullpath = path.join('./data/advocates/', filepath)
    if path.isfile(fullpath):
        with open(fullpath, 'r') as file:
            advocates.append(yaml.safe_load(file))


advocates_list_items = [news_item_template
                        .replace('{{ url }}', advocate.get('website'))
                        .replace('{{ title }}', advocate.get('name'))
                        for advocate in advocates]

advocates_list = list_template.replace('{{ items }}',
                                       ''.join(advocates_list_items))

html = (html_template.replace('{{ news }}', news_list)
                     .replace('{{ advocates }}', advocates_list))

with open('docs/index.html', 'w', encoding='utf8') as html_file:
  html_file.write(html)
