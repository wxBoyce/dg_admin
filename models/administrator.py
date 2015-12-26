#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import hashlib

from models.basic import Basic


class Administrator(Basic):
    def __init__(self):
        super(Administrator, self).__init__()

    def create_new_user(self, nickname, pwd):
        if not self.checkout_nickname_unique(nickname):
            return False
        pwd = hashlib.md5(pwd).hexdigest()
        sql = "insert into users (nickname, password, created_at, shopname, role) value ('%s', '%s', '%s', '', 'user')" \
              % (nickname, pwd, time.strftime('%Y-%m-%d'))
        self.g_mysql.execute(sql)
        return True

    def checkout_nickname_unique(self, nickname):
        sql = "select id from users where nickname='%s'" % nickname
        ret = self.g_mysql.get(sql)
        if not ret:
            return True
        return False
