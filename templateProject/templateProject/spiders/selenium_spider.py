import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy import Spider
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumSpider(scrapy.Spider):
    name = 'selenium_spider'
    start_urls = ['https://google.com']

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")


    
    def start_requests(self):
        self.driver.get('https://example.com')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))
        )
        yield scrapy.Request(url=self.driver.current_url, callback=self.parse)


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

    def parse2(self, response):
        self.driver.find_element_by_css_selector('input[name="username"]').send_keys('myusername')
        self.driver.find_element_by_css_selector('input[name="password"]').send_keys('mypassword')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.my-result'))
        )
        selector = Selector(text=self.driver.page_source)
        result = selector.css('div.my-result::text').get()
        yield {'result': result}

    def closed(self, reason):
        self.driver.quit()
