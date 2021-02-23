class Recommend:

    def __init__(self):

        self.content = ''
        self.publish_time = ''
        self.origin_id = ''
        self.mid = ''
        self.pics = ''
        self.origin_url = ''

        self.user_name = ''
        self.user_id = ''
        self.avatar = ''
        self.verified = 0
        self.verified_reason = ''
        self.user_url = ''

        self.up_num = 0
        self.retweet_num = 0
        self.comment_num = 0

        self.retweeted_id = ''
        self.retweeted_mid = ''
        self.retweeted_publish_time = ''
        self.retweeted_text = ''
        self.retweeted_textLength = 0
        self.retweeted_pics = ''
        self.retweeted_user_name = ''
        self.retweeted_user_id = ''
        self.retweeted_avatar = ''
        self.retweeted_verified = 0
        self.retweeted_verified_reason = ''
        self.retweeted_user_url = ''

    def __str__(self):
        """打印一条微博"""
        result = self.content + '\n'
        result += u'origin_id：%s\n' % self.origin_id
        result += u'发布时间：%s\n' % self.publish_time
        result += u'点赞数：%d\n' % self.up_num
        result += u'转发数：%d\n' % self.retweet_num
        result += u'评论数：%d\n' % self.comment_num
        result += u'原文链接：%s\n' % self.origin_url
        return result
