#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basic import BasicHandler, login


class IndexHandler(BasicHandler):

    @login
    def get(self):
        page = self.get_argument('page', 1)
        extra_info = self.user_ins.fetch_user_info_by_nickname(self.current_user)
        goods_info_list = list()
        tmp_list = self.index_ins.fetch_goods_list_by_current_user(int(page))
        for it in tmp_list:
            it['owner'] = self.current_user
            it['created_at'] = str(it['created_at'])
            goods_info_list.append(it)
        total_page = (self.index_ins.count_goods_num_for_user() + self.index_ins.count - 1)/self.index_ins.count
        self.render('index.html', extra_info=extra_info, total_page=total_page, cur_page=int(page),
                    goods_info_list=goods_info_list)


class SearchHandler(BasicHandler):

    @login
    def get(self):
        goodsname = self.get_argument("goodsname", None)
        if not goodsname:
            return
        extra_info = self.user_ins.fetch_user_info_by_nickname(self.current_user)
        tmp_list = self.search_ins.get_goods_info_by_goods_name(goodsname)
        if not tmp_list:
            return self.redirect("/goods/create")
        goods_info_list = list()
        for item in tmp_list:
            item['owner'] = extra_info['nickname']
            item['created_at'] = str(item['created_at'])
            goods_info_list.append(item)
        self.render('index.html', extra_info=extra_info, total_page=1, cur_page=1,
                    goods_info_list=goods_info_list)

