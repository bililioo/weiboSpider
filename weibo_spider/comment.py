class Comment:
    def __init__(self):

        self.text = ''
        self.publish_time = ''
        self.origin_id = ''
        self.mid = ''
        self.rootid = ''
        self.rootidstr = ''
        self.sub_comments = 0 # 子评论数量
        self.max_id = ''
        self.like_count = 0

        self.origin_url = ''
        self.content_id = ''

        self.user_name = ''
        self.user_id = ''
        self.avatar = ''
        self.verified = 0
        self.verified_reason = ''
        self.user_url = ''

    def __str__(self):
        """打印一条评论"""
        result = u'评论：%s\n' % self.origin_id
        result += self.text + '\n'
        result += "content_id：%s\n" % self.content_id
        result += u'发布时间：%s\n' % self.publish_time
        result += u'原文链接：%s\n' % self.origin_url
        return result
