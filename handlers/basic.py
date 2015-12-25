#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

from models.goods import Goods


class BasicHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BasicHandler, self).__init__(application, request, **kwargs)
        self.goods_ins = Goods()

    def user_info_via_id(self, uid):
        user_info = {
            'uid': uid,
            'nickname': 'Boyce',
            'role': 'Administrator',
            'avatar': None,
        }
        return user_info

