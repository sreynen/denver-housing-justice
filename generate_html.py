#!/usr/bin/env python3

import json

with open('./docs/feed.json', 'r', encoding='utf8') as file:
  news = json.load(file)

with open('./templates/index.html', 'r', encoding='utf8') as file:
  html_template = file.read()

with open('./templates/list.html', 'r', encoding='utf8') as file:
  list_template = file.read()

with open('./templates/list-news-item.html', 'r', encoding='utf8') as file:
  news_item_template = file.read()

list_items = [news_item_template
              .replace('{{ url }}', item.get('url'))
              .replace('{{ title }}', item.get('title'))
              for item in news.get('items', [])]
news_list = list_template.replace('{{ items }}',
                                  ''.join(list_items))
html = html_template.replace('{{ news }}', news_list)

with open('docs/index.html', 'w', encoding='utf8') as html_file:
  html_file.write(html)
