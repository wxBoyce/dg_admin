#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.basic import BasicHandler


class GoodsHandler(BasicHandler):

    def get(self, action):
        if action == 'create':
            extra_info = self.user_info_via_id(1)
            goods_info = {
                "id": 0,
                "owner": extra_info['nickname'],
                "goodsname": '',
                "picurls": ['', '', ''],
                "goodsdesp": '',
                "price": '',
                "created_at": '',
            }
            extra_info['title'] = "Create-New_Goods"
            return self.render('single.html', goods_info=goods_info, extra_info=extra_info)

    def post(self, action):
        if action == 'create':
            print self.get_argument("owner", "")
            print self.get_argument("goodsname", "")

