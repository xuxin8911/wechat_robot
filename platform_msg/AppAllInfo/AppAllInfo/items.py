# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


#class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
 #   pass

class FeiXiaoHaoItem(Item):
	urlmd5id = Field()
	updated = Field()
	name = Field()
	chineseName =  Field()
	engName =  Field()
	cnyPrice =  Field()
	usdtPrice =  Field()
	btcPrice =  Field()
	upMarkets =  Field()
	releaseTime =  Field()
	whitePaper =  Field()
	site =  Field()
	blockite =  Field()
	concept =  Field()

class BinanceNewItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class BigoneNewItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class ZBNoticeItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()


class BcexNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class CexNoticesItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class ZBNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class CoinwNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class CoineggNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class CoolcoinNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class BtcTradeNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class BitfinexNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()


class BittrexNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class ExxNewsItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()


class HuobiItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class GateItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()

class OkexItem(Item):
    urlmd5id = Field()
    updated = Field()
    title = Field()
    content = Field()
    url = Field()


class BiShiJieItem(Item):
    urlmd5id = Field()
    updated = Field()
    content_today = Field()
    #content_yestoday = Field()
    url = Field()
