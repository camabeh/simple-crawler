# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log(f'I just visied {response.url}')

        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }

        # follow pagination
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        next_page_url = response.urljoin(next_page_url)
        # create request for new page
        yield scrapy.Request(url=next_page_url, callback=self.parse)