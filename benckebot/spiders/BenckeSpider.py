# -*- coding: utf-8 -*-
import scrapy
import re
from benckebot.items import BenckebotItem


class BenckeSpider(scrapy.Spider):
    name = 'bencke'
    allowed_domains = ['dba.dk']
    start_urls = ['https://www.dba.dk/boliger/andelsbolig/andelslejligheder/reg-koebenhavn-og-omegn/']

    def parse(self, response):
        listOfLinks = response.css("a.link-to-listing::attr(href)").extract()
        for link in listOfLinks:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.enterPage)

    def enterPage(self, response):
        item = BenckebotItem()
        item["id"] = response.css("h1::text").extract_first()
        item["url"] = response.url
        item["zipCode"] = 0000
        item["price"] = re.sub("\\D*", "", response.css("span.price-tag::text").extract_first())
        info = response.css("table td::text").extract()
        i = 0
        while i < len(info):
            if info[i] == "Månedlig ydelse":
                item["expenses"] = re.sub("\\D*", "", info[i + 1])
            elif info[i] == "Postnr.":
                item["zipCode"] = re.sub("\\D*", "", info[i + 1])
            i += 1
        return item


