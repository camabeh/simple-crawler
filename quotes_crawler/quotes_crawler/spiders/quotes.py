# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        # extract csrf token value
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        # python dictionary with form values
        form = {
            'csrf_token': token,
            'username': 'abc',
            'password': 'abc',
        }
        # submit a POST request
        yield scrapy.FormRequest(url=self.login_url, formdata=form, callback=self.parse_quotes)

    def parse_quotes(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author_name': quote.css('small.author::text').extract_first(),
                'author_url': quote.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first(),
            }

        # follow pagination
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        next_page_url = response.urljoin(next_page_url)
        # create request for new page
        yield scrapy.Request(url=next_page_url, callback=self.parse_quotes)
