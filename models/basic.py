#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbmanage import global_mysql


class Basic(object):
    def __init__(self):
        super(Basic, self).__init__()
        self.g_mysql = global_mysql
