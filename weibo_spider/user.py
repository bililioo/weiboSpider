class User:
    def __init__(self):
        self.user_id = ''
        self.nickname = ''
        self.profile_url = ''
        self.avatar = ''
        self.verified = 0
        self.verified_reason = ''
        self.user_url = ''

        self.gender = ''
        self.location = ''
        self.birthday = ''
        self.description = ''
        self.verified_reason = ''
        self.talent = ''

        self.education = ''
        self.work = ''

        self.weibo_num = 0
        self.following = 0
        self.followers = 0

    def __str__(self):
        """打印微博用户信息"""
        result = ''
        result += u'用户昵称: %s\n' % self.nickname
        result += u'用户id: %s\n' % self.id
        result += u'微博数: %d\n' % self.weibo_num
        result += u'关注数: %d\n' % self.following
        result += u'粉丝数: %d\n' % self.followers
        return result
