# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from scrapy.shell import inspect_response
import re
# import csv

class AddiehuSpider(scrapy.Spider):
    name = 'addiehu'
    allowed_domains = ['addi.ehu.es']
    start_urls = ['https://addi.ehu.es/handle/10810/2017/discover?query=%22Grado+en+Ingenier%C3%ADa+Inform%C3%A1tica%22&submit=&rpp=10&sort_by=dc.date.issued_dt&order=desc']

    # outfile = open("output.csv", "w")
    # writer = csv.writer(outfile)

    tabsnewlines = re.compile(r"[\n\t]*")

    def clean(self, selector):
        value = selector.extract_first()
        if not value:
            value = ""
        return self.tabsnewlines.sub("", value.encode('utf-8'))

    def parse(self, response):
        for project in response.css('div.col-sm-9.artifact-description'):
            link = self.clean(project.css('a::attr(href)'))
            title = self.clean(project.css('a > h4 ::text'))
            author = self.clean(project.css('div.artifact-info > span.author.h4 > small > span ::text'))
            date = self.clean(project.css('div.artifact-info > span.publisher-date.h4 > small > span ::text'))
            detailspage = 'https://' + self.allowed_domains[0] + link + '?show=full'
            # print(detailspage)
            request = Request(detailspage, callback = self.visit_details)
            request.meta['item'] = { 'link': link , 'title': title, 'author': author, 'date': date }
            yield request
            for next_page in response.css('a.next-page-link'):
                yield response.follow(next_page, self.parse)

    def visit_details(self, response):
        item = response.meta['item']

        ind = 0
        for enlace in response.css('div.file-link > a ::attr(href)').extract():
            item['linkdetail' + str(ind)] = enlace
            ind = ind + 1
        # inspect_response(response, self)
        for dc in response.css('tr.ds-table-row'):
            clave = self.clean(dc.css('td.label-cell ::text'))
            valor = self.clean(dc.css('td.word-break ::text'))
            print(clave + ":" + valor)
            item[clave] = valor
        # self.writer.writerow( item.values() )        
        yield item

    def close(self):
     #   self.outfile.close()
        print("-----Check to see if this is closed-----")
