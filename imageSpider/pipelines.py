# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class ImagespiderPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        return scrapy.Request(item['url'], meta={"title": item['title']})
    
    def file_path(self, request, response=None, info=None):
        path = super().file_path(request, response=response, info=info)
        path = path.replace("full", response.meta['title'])
        return path