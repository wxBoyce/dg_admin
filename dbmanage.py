#!/usr/bin/env python
# -*-coding:utf-8-*-

import srvconf
import torndb
import pymongo

# mysql 数据库全局链接
global_mysql = torndb.Connection(srvconf.MYSQL_HOST, srvconf.MYSQL_DB, srvconf.MYSQL_USER, srvconf.MYSQL_PASSWORD)

# mongodb 数据库全局链接
global_mongodb = pymongo.MongoClient(srvconf.MONGODB_HOST, srvconf.MONGODB_PORT).test
