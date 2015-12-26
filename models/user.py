#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

from models.basic import Basic


class Users(Basic):
    def __init__(self):
        super(Users, self).__init__()

    def checkout_user_login(self, nickname, pwd):
        sql = "select id, password from users where nickname='%s'" % nickname
        ret = self.g_mysql.get(sql)
        if not ret:
            return False
        if hashlib.md5(pwd).hexdigest() != ret['password']:
            return False
        return True

    def fetch_user_info_by_nickname(self, nickname):
        sql = "select id, nickname, password, wechat, qq, email, avatar, shopname, shopdesp, password, role from users " \
              "where nickname='%s'" % nickname
        return self.g_mysql.get(sql)

    def update_user_pwd(self, nickname, pwd):
        sql = "update users set password='%s' where nickname='%s'" % (pwd, nickname)
        self.g_mysql.execute(sql)

    def update_user_info(self, user_info):
        sql = "update users set wechat='%s', email='%s', qq='%s' where nickname='%s'" % user_info
        self.g_mysql.execute(sql)

    def update_user_shop(self, shop_info):
        sql = "update users set shopname='%s', shopdesp='%s' where nickname='%s'" % shop_info
        self.g_mysql.execute(sql)
