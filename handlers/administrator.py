#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basic import BasicHandler, admin


class AdministratorHandler(BasicHandler):

    @admin
    def get(self):
        self.render("admin.html")

    @admin
    def post(self):
        username = self.get_argument("user_name", None)
        pwd = self.get_argument("pwd", None)
        if not username or not pwd:
            return self.write("密码或者用户名不能为空!!!")
        if self.admin_ins.create_new_user(username, pwd):
            return self.write("添加成功!!")
        return self.write("创建失败!!")
