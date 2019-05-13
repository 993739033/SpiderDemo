import scrapy

from SpiderDemo.items import MKItem
##简单爬虫使用

class MKSprider(scrapy.Spider):
    name = "MKSprider"

    allowed_domains = ["imooc.com"]
    start_urls = ["http://www.imooc.com/course/list"]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        with open("SpriderBean", 'w', encoding="utf-8") as f:
            f.write("爬取到的数据\n")

        item = MKItem()
        print(">>>>>>>>")
        for box in response.xpath('//*[@id="main"]/div[2]/div[2]/div[1]/div/div'):
            hrefm = box.xpath('./a/@href').extract()[0]
            print(hrefm)
            item["m_url"] = "http://www.imooc.com" + str(box.xpath('./a//@href').extract()[0])
            item["image_url"] = str(box.xpath('./a/div/img/@src').extract()[0])
            item["image_big_url"] = str(box.xpath('./a/div/img/@data-original').extract()[0])
            title = str(box.xpath('./a/div/h3/text()').extract()[0])
            print("title>>", title)
            item["title"] = title

            print(item["m_url"])
            with open("SpriderBean", 'a', encoding="utf-8") as f:
                f.write(item.get("m_url") + "\n")
                f.write(item.get("image_url") + "\n")
                f.write(item.get("image_big_url") + "\n")
                f.write(item.get("title") + "\n")
                f.write("\n")
            yield item
