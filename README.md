## Simple spider project

1. Experiment phrase
`scrapy shell http://quotes.toscrape/random`

2. Generate simple scraper
`scrapy genspider quotes toscrape.com`

3. Run
`scrapy runspider quotes.py -o`
 
4. Save output to file 
`scrapy runspider quotes.py -o items.json` 
---
## Robust spider project
1. Generate spider project
`scrapy startproject quotes_crawler  `

2. List spiders in project
`scrapy list`

3. Run specific crawler
`scrapy crawl quotes`
---
From tutorial:
`https://www.youtube.com/watch?v=vkA1cWN4DEc&list=PLZyvi_9gamL-EE3zQJbU5N3nzJcfNeFHU&index=1`