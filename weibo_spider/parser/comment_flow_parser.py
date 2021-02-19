import logging
import random
from time import sleep
from weibo_spider.comment import Comment

from .parser import Parser
from .util import handle_garbled, handle_html, handle_json

logger = logging.getLogger('spider.comment_parser')


class CommentFlowParser(Parser):
    def __init__(self, cookie, origin_id, mid):
        self.cookie = cookie
        self.url = 'https://m.weibo.cn/comments/hotflow?id=%s&mid=%s&max_id_type=0' % (origin_id, mid)
        logger.debug(self.url)
        self.comment_list = handle_json(self.cookie, self.url)

    def handleComments(self):
        """处理评论内容"""
        try:
            comments = []
            data = self.comment_list['data']['data']
            for d in data:
                comment = Comment()
                comment.origin_id = d['id']
                comment.mid = d['mid']
                comment.publish_time = d['created_at']
                comment.rootid = d['rootid']
                comment.rootidstr = d['rootidstr']
                comment.text = d['text']
                comment.origin_url = 'https://m.weibo.cn/comments/hotflow?id=%s&mid=%s&max_id_type=0' % (comment.origin_id, comment.mid)

                comment.verified = 0
                if 'verified_reason' in d['user']:
                    comment.verified_reason = d['user']['verified_reason']
                    comment.verified = 1
                
                comment.avatar = d['user']['profile_image_url']
                comment.user_url = d['user']['profile_url']
                comment.user_id = d['user']['id']
                comment.user_name = d['user']['screen_name']

                comment.max_id = d['max_id']
                comment.like_count = d['like_count']
                
                comments.append(comment)
                logger.info(comment)
            return comments

        except Exception as e:
            logger.exception(e) 
