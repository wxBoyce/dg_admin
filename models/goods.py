#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import bson.binary
import bson.objectid
from cStringIO import StringIO
from PIL import Image

from models.basic import Basic
from dbmanage import global_mongodb


class Goods(Basic):
    def __init__(self):
        super(Goods, self).__init__()
        self.g_mongodb = global_mongodb

    def store_pic_file(self, f, _id=None):
        content = StringIO(f)
        try:
            mime = Image.open(content).format.lower()
        except IOError:
            return
        if not _id:
            c = dict(content=bson.binary.Binary(content.getvalue()), mime=mime)
            self.g_mongodb.files.save(c)
        else:
            c = dict(content=bson.binary.Binary(content.getvalue()), mime=mime)
            self.g_mongodb.files.remove({'_id': _id})
            self.g_mongodb.files.save(c)
        return c['_id']

    def create_goods_info(self, goods_info):
        sql = "insert into goods (goodsname, price, goodsdesp, created_at, owner, picurls, content, status) " \
              "values ('%s','%s','%s','%s',%d,'%s','%s','%s')" % goods_info
        return self.insert_info_to_mysql(sql)

    def update_goods_info(self, goods_info):
        sql = "update goods set goodsname='%s', price='%s', goodsdesp='%s', updated_at='%s', picurls='%s', content='%s'" % goods_info
        return self.g_mysql.execute(sql)

    def fetch_goods_info_by_id(self, goods_id):
        sql = "select * from goods where id=%s"
        return self.g_mysql.get(sql, goods_id)

    def set_goods_status_by_id(self, goods_id, action):
        if action == 'active':
            sql = "update goods set status='ok', updated_at='%s' where id=%s" % (time.strftime('%Y-%m-%d'), goods_id)
        elif action == 'shield':
            sql = "update goods set status='err', updated_at='%s' where id=%s" % (time.strftime('%Y-%m-%d'), goods_id)
        self.g_mysql.execute(sql)
