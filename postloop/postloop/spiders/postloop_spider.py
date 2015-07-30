__author__ = 'tony'
from scrapy.spider import Spider
from scrapy.log import ScrapyFileLogObserver
from scrapy import log, Selector



class PostloopSpider(Spider):
    name = 'postloop'
    start_urls = ['http://portal.postloop.com/index.php?forums/health-fitness.22/',]
    allowed_domains = ['postloop.com',]

    def __init__(self, name=None, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=log.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=log.ERROR).start()
        super(PostloopSpider, self).__init__(name, **kwargs)

    def parse(self, response):
        sel = Selector(response)

        ITEM_SEL_XPATH = '//ol[@class="discussionListItems"]/li'

        item_sels = sel.xpath(ITEM_SEL_XPATH)
        if item_sels:
            TITLE_XPATH = './/h3[@class="title"]/a/text()'
            for item_sel in item_sels:

        else:
            return