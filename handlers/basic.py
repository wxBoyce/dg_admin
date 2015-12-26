#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import tornado.web

from models.goods import Goods
from models.user import Users
from models.index import Index, Search
from models.administrator import Administrator


class BasicHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BasicHandler, self).__init__(application, request, **kwargs)
        self.goods_ins = Goods()
        self.index_ins = Index()
        self.search_ins = Search()
        self.user_ins = Users()
        self.admin_ins = Administrator()

    def user_info_via_nickname(self, nickname):
        tmp_info = self.user_ins.fetch_user_info_by_nickname(nickname)
        user_info = {
            'uid': tmp_info['id'],
            'nickname': tmp_info['nickname'],
            'role': tmp_info['role'],
            'avatar': tmp_info['avatar'],
        }
        return user_info

    # 存储用户的登录信息
    def set_session(self, user, days=1):
        self.set_secure_cookie("_auid", str(user['name']), expires_days=days, httponly=True)
        self.set_secure_cookie("_auth", str(user['pwd']), expires_days=days, httponly=True)

    def del_session(self):
        self.clear_cookie("_auid")
        self.clear_cookie("_auth")

    # 重写get_current_user
    def get_current_user(self):
        username = self.get_secure_cookie('_auid')
        auth = self.get_secure_cookie('_auth')
        if username and auth:
            ret = self.user_ins.fetch_user_info_by_nickname(username)
            if auth == ret['password']:
                return username


def login(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):

        if not self.current_user:
            if 'Accept' in self.request.headers and self.request.headers['Accept'].find('json') >= 0:
                self.redirect('/login')
                return
            if self.request.method in ("GET", "HEAD"):
                self.redirect('/login')
                return
            self.write("验证用户错误!!")
            return
        return method(self, *args, **kwargs)
    return wrapper


def admin(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):

        if self.current_user != 'super':
            self.write("您没有操作权限!!")
            return
        return method(self, *args, **kwargs)
    return wrapper



