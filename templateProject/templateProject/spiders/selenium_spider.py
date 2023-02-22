import scrapy
from selenium import webdriver
from scrapy.selector import Selector

class SeleniumSpider(scrapy.Spider):
    name = 'selenium_spider'
    start_urls = ['https://google.com']

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

    def parse(self, response):
        self.driver.get(response.url)

        # Wait for the page to load
        self.driver.implicitly_wait(10)

        # Extract data using Selenium
        element = self.driver.find_element_by_css_selector('#my-element')
        text = element.text

        # Use Scrapy's Selector to parse the response
        selector = Selector(text=text)
        data = selector.css('p::text').get()

        yield {
            'data': data
        }

    def closed(self, reason):
        self.driver.quit()
