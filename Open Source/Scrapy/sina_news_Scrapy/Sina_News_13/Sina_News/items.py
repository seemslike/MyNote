# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import sys

#处理编码问题
reload(sys)
sys.setdefaultencoding( "utf-8" )

class SinaNewsItem(Item):
    """存储提取信息数据结构"""

    # define the fields for your item here like:
    # name = scrapy.Field()
    news_dict_list_str = Field()

