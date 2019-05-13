import scrapy

class myScr(scrapy.Spider):
    name = "myScr"#设置全局唯一name
    host = "https://www.baidu.com"
    start_urls=("https://www.baidu.com",)

    def parse(self, response):
        print(response.body)