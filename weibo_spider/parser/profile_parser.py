import logging
from logging import log
from os import stat
import random
from time import sleep
from typing import List
from weibo_spider.user import User
from weibo_spider.recommend import Recommend


from .parser import Parser
from .util import handle_garbled, handle_html, handle_json

logger = logging.getLogger('spider.Profile')

class Profile(Parser):
    def __init__(self, cookie, uid):
        self.cookie = cookie
        self.uid = uid
        self.url = 'https://m.weibo.cn/profile/info?uid=%s' % uid
        self.content_list = handle_json(self.cookie, self.url)

    def handleContents(self):
        """解析获取的个人微博主页"""
        try:
            recommends = []
            userDict = self.content_list['data']['user']
            user = User()
            user.verified = 0
            if 'verified_reason' in userDict:
                    user.verified_reason = userDict['verified_reason']
                    user.verified = 1
                
                    user.avatar = userDict['profile_image_url']
                    user.user_url = userDict['profile_url']
                    user.user_id = userDict['id']
                    user.nickname = userDict['screen_name']

            statuses = self.content_list['data']['statuses']
            for status in statuses:
                recommend = Recommend()
                recommend.origin_id = status['id']
                recommend.mid = status['mid']
                recommend.publish_time = status['created_at']
                recommend.content = status['text']
                recommend.origin_url = 'https://m.weibo.cn/detail/%s' % status['id']

                recommend.verified = 0
                if 'verified_reason' in status['user']:
                    recommend.verified_reason = status['user']['verified_reason']
                    recommend.verified = 1
                
                recommend.avatar = status['user']['profile_image_url']
                recommend.user_url = status['user']['profile_url']
                recommend.user_id = status['user']['id']
                recommend.user_name = status['user']['screen_name']

                recommend.retweet_num = status['reposts_count']
                recommend.comment_num = status['comments_count']
                recommend.up_num = status['attitudes_count']

                if 'pics' in status:
                    urls = []
                    for pic in status['pics']:
                        urls.append(pic['url'])
                    recommend.pics = ','.join(urls)
                    recommends.append(recommend)
                logger.info(recommend)
            return recommends

        except Exception as e:
            logger.exception(e) 