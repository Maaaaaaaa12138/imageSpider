import scrapy
from imageSpider.items import ImagespiderItem

class spider(scrapy.Spider):

    name = "imageSp1"

    def start_requests(self):
        for i in range(1, 50):
            yield scrapy.Request(f"http://www.bizhi88.com/3840x2160/{i}.html", meta={"title": "4K壁纸"})
    
    # parse回调函数
    def parse(self, response):
        imageUrls = [i.split("?")[0] for i in response.xpath("//div[@class='item']/a/img/@data-original").extract()]
        for url in imageUrls:
            yield ImagespiderItem(url=url, title=response.meta['title'])