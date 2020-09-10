import scrapy

class Project(scrapy.Item):
    title = scrapy.Field()
    architects = scrapy.Field()

class Gallery(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
