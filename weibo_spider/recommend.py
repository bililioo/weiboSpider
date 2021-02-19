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

    def __str__(self):
        """打印一条微博"""
        result = self.content + '\n'
        result += u'发布时间：%s\n' % self.publish_time
        result += u'点赞数：%d\n' % self.up_num
        result += u'转发数：%d\n' % self.retweet_num
        result += u'评论数：%d\n' % self.comment_num
        result += u'原文链接：%s\n' % self.origin_url
        return result
