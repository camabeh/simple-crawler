# -*- coding: utf-8 -*-
import json

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    api_url = 'http://quotes.toscrape.com/api/quotes?page='
    start_urls = [f'{api_url}1']

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                'author_name': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags'],
            }

        if data['has_next']:
            next_page_num = data['page'] + 1
            yield scrapy.Request(url=response.urljoin(f'{self.api_url}{next_page_num}'), callback=self.parse)