#!/usr/bin/env python
# -*-coding:utf-8-*-

import srvconf
import torndb

global_mysql = torndb.Connection(srvconf.MYSQL_HOST, srvconf.MYSQL_DB, srvconf.MYSQL_USER, srvconf.MYSQL_PASSWORD)
