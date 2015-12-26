#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basic import BasicHandler, login


class UserHandler(BasicHandler):

    @login
    def get(self, action):
        extra_info = self.user_ins.fetch_user_info_by_nickname(self.current_user)
        self.render('account.html', extra_info=extra_info)

    @login
    def post(self, action):
        wechat = self.get_argument("wechat_name", '')
        qq = self.get_argument("QQ_number", '')
        email = self.get_argument("email", '')

        pwd1 = self.get_argument("password1", None)
        pwd2 = self.get_argument("password2", None)

        shopname = self.get_argument("shop_name", '')
        shopdesp = self.get_argument("shop_introduction", '')

        if action == 'profile':
            if not wechat and not qq and not email:
                return self.redirect('/user/shop')
            user_info = (
                wechat, email, qq, self.current_user
            )
            self.user_ins.update_user_info(user_info)
            if pwd1 and pwd2 and pwd1 == pwd2:
                self.user_ins.update_user_pwd(self.current_user, pwd1)
                self.del_session()
                return self.redirect('/login')
        elif action == 'shop':
            if not shopname and not shopdesp:
                return self.redirect('/user/profile')
            shop_info = (
                shopname, shopdesp, self.current_user
            )
            self.user_ins.update_user_shop(shop_info)
            return self.redirect('/user/shop')

        return self.redirect('/user/profile')
