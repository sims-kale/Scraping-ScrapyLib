import scrapy
from openpyxl import load_workbook
from scrapy.crawler import CrawlerProcess

class WebscrapingSpider(scrapy.Spider):
    name = "webscraping"
    

    def start_requests(self):
        for link in self.links:
            yield scrapy.Request(url=link, callback=self.parse)


    def parse(self, response):
        title = response.css("._44qnta > span:nth-child(1)").get_attribute("innerText")
        with open('output.txt', 'a') as f:
            f.write(title + '\n')

    if __name__ == '__main__':

        excelfile = load_workbook('E-commerce URL.xlsx')
        sheet = excelfile.active
        links = [cell.value for cell in sheet['A1:Z120'] if cell.value is not None]

        process = CrawlerProcess()
        process.crawl(start_requests, links=links)
        process.start()

       