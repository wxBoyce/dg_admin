#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbmanage import global_mysql


class Basic(object):
    def __init__(self):
        super(Basic, self).__init__()
        self.g_mysql = global_mysql

    def insert_info_to_mysql(self, sql):
        return self.g_mysql.insert(sql)

