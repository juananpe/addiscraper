# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.shell import inspect_response
import re
from addi.items import AddiItem
from scrapy.loader import ItemLoader
# import csv

class AddiehuSpider(scrapy.Spider):
    name = 'addiehu'
    allowed_domains = ['addi.ehu.es']
    start_urls = ['https://addi.ehu.es/handle/10810/2017/discover?order=desc&rpp=10&sort_by=dc.date.issued_dt&page=1&query=%22Grado+en+Ingenier%C3%ADa+Inform%C3%A1tica%22&group_by=none&etal=0']
    repo = 2 # addi.ehu.es 

    # outfile = open("output.csv", "w")
    # writer = csv.writer(outfile)

    tabsnewlines = re.compile(r"[\n\t]*")

    def clean(self, selector):
        value = selector.extract_first()
        if not value:
            value = ""
        return self.tabsnewlines.sub("", value) #.encode('utf-8'))

    def parse(self, response):
        for project in response.css('div.col-sm-9.artifact-description'):
            link = self.clean(project.css('a::attr(href)'))
            title = self.clean(project.css('a > h4 ::text'))
            author = self.clean(project.css('div.artifact-info > span.author.h4 > small > span ::text'))
            date = self.clean(project.css('div.artifact-info > span.publisher-date.h4 > small > span ::text'))
            detailspage = 'https://' + self.allowed_domains[0] + link + '?show=full'
            # print(detailspage)
            request = Request(detailspage, callback = self.visit_details)
            request.meta['item'] = { 'link': link , 'project': title, 'author': author, 'date': date }
            yield request
            for next_page in response.css('a.next-page-link'):
                yield response.follow(next_page, self.parse)

    def visit_details(self, response):
        item = response.meta['item']

        links = []
        #aspect_artifactbrowser_ItemViewer_div_item-view div > a
        for enlace in response.css('#aspect_artifactbrowser_ItemViewer_div_item-view div > a ::attr(href)').extract():
            links.append(enlace)
        # FIXME: llega link pero no se usa... en links también está
        loader = ItemLoader(item=AddiItem())
        loader.add_value('author', item['author'])
        loader.add_value('date', item['date'])
        loader.add_value('project', item['project'])
        loader.add_value('links', links)
        loader.add_value('repo',self.repo)
        # inspect_response(response, self)

        yield loader.load_item()


        yield item

    def close(self):
     #   self.outfile.close()
        print("-----Check to see if this is closed-----")
