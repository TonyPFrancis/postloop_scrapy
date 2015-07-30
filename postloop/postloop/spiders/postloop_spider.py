__author__ = 'tony'
from scrapy.spider import Spider
from scrapy.log import ScrapyFileLogObserver
from scrapy import log, Selector
from postloop.items import PostloopItem

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
            USER_XPATH = './/a[@title="Thread starter"]/text()'
            for item_sel in item_sels:
                title = item_sel.xpath(TITLE_XPATH).extract()
                title = title[0].strip() if title else ''
                user_name = item_sel.xpath(USER_XPATH).extract()
                user_name = user_name[0].strip() if user_name else ''
                item = PostloopItem()
                item['title'] = title
                item['user_name'] = user_name
                yield item
        else:
            return

        NEXT_PAGE_XPATH = '//div[@class="PageNav"]//a[text()="Next >"]/@href'