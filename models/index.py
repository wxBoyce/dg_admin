#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.basic import Basic


class Index(Basic):
    def __init__(self):
        super(Index, self).__init__()
        self.count = 30

    def fetch_goods_list_by_current_user(self, page):
        user_id = 1
        sql = "select id, goodsname, picurls, goodsdesp, created_at, status from goods where owner=%s order " \
              "by id desc limit %s, %s" % (user_id, (page-1)*self.count, self.count)
        return self.g_mysql.query(sql)

    def count_goods_num_for_user(self):
        user_id = 1
        sql = "select id from goods where owner=%s" % user_id
        ret = self.g_mysql.query(sql)
        return len(ret)


class Search(Basic):
    def __init__(self):
        super(Search, self).__init__()

    def get_goods_info_by_goods_name(self, goodsname):
        user_id = 1
        sql = "select id, goodsname, picurls, goodsdesp, created_at, status from goods where " \
              "goodsname like '%%%%%s%%%%' and owner=%s" % (goodsname, user_id)
        return self.g_mysql.query(sql)
