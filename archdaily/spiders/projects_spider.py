import scrapy
import shutil
import os
from pathlib import Path
from archdaily.items import Project, Gallery


class ProjectsSpider(scrapy.Spider):
    name = 'projects'
    f = open("urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
    project_title = []

    def parse(self, response):
        self.category = str(response.xpath(
            '//*[@id="content"]/div/div[2]/div[2]/ol/li[3]/a/span/text()').extract_first())
        title = str(response.xpath(
            '//h1/text()').extract_first().split(' /', 1)[0].replace('\n', ''))
        architects = str(response.xpath(
            '//span[@class="afd-specs__key" and contains(text(), "Architects")]/..//span/a/text()').extract_first())
        self.project_title = architects+'-'+title
        location = str(response.xpath(
            '//span[@class="afd-specs__key" and contains(text(), "Location")]/..//span/a/text()').extract_first()).replace('  ', ' ')
        area = str(response.xpath(
            '//span[@class="afd-specs__key" and contains(text(), "Area")]/..//span/a/text()').extract_first()).replace('"', '').replace('\n', '')
        project_year = str(response.xpath(
            '//span[@class="afd-specs__key" and contains(text(), "Year")]/..//span/a/text()').extract_first()).replace('"', '').replace('\n', '').replace('          ', '')
        f = open("images/full/caption.txt", "w", encoding='utf-8')
        text = """Title: """+title+"""
Architects: """+architects+"""
Location: """+location+"""
Area: """+area+"""
Year: """+project_year+"""
"""
        f.write(text)
        for href in response.css(".gallery-thumbs-link::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        src = str(response.css(
            'meta[property="og:image"]::attr(content)').extract_first()).split('?', 1)[0]
        url = response.urljoin(src)
        yield Gallery(file_urls=[url])

    def closed(self, reason):
        Path('projects/' +self.category+"/"+self.project_title).mkdir(parents=True, exist_ok=True)
        source = 'images/full/'
        dest = 'projects/' + \
            self.category+"/"+self.project_title
        files = os.listdir(source)
        for f in files:
            shutil.move(source+f, dest)
