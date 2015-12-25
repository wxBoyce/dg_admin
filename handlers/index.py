#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basic import BasicHandler


class IndexHandler(BasicHandler):
    def get(self):
        extra_info = self.user_info_via_id(1)
        self.render('account.html', extra_info=extra_info, total_page=20, cur_page=1)
