import scrapy


class GeneralspiderSpider(scrapy.Spider):
    name = "generalSpider"
    allowed_domains = ["www.google.com"]
    start_urls = ["http://www.google.com/"]

    def parse(self, response):
        pass
