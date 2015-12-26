#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from handlers.basic import BasicHandler, login


class GoodsHandler(BasicHandler):

    @login
    def get(self, action):
        if action == 'create':
            extra_info = self.user_info_via_nickname(self.current_user)
            goods_info = {
                "id": 0,
                "owner": extra_info['nickname'],
                "goodsname": '',
                "picurls": ['', '', ''],
                "goodsdesp": '',
                "price": '',
                "created_at": '',
                "content": '',
            }
            extra_info['title'] = "Create-New_Goods"
            return self.render('single.html', goods_info=goods_info, extra_info=extra_info)
        elif action == 'view':
            goods_id = self.get_argument('id', None)
            if not goods_id:
                return
            extra_info = self.user_info_via_nickname(self.current_user)
            extra_info['title'] = "Single-Goods-Info"
            goods_info = self.goods_ins.fetch_goods_info_by_id(goods_id)
            if not goods_info:
                return self.write("商品不存在!!")
            goods_info['owner'] = extra_info['nickname']
            pic_url = goods_info['picurls'].split('|')
            pic_url_list = list()
            for it in pic_url:
                if not it:
                    pic_url_list.append(it)
                    continue
                pic_url_list.append("http://localhost:10081/img/%s" % it)
            goods_info['picurls'] = pic_url_list
            return self.render('single.html', goods_info=goods_info, extra_info=extra_info)

    @login
    def post(self, action):

        goodsname = self.get_argument("goodsname", "")
        goodsdesp = self.get_argument("goodsdesp", "")
        price = self.get_argument("price", "")
        content = self.get_argument("content", "")

        if action == 'create':
            ret_user = self.user_ins.fetch_user_info_by_nickname(self.current_user)
            if not goodsname:
                return self.write("创建的商品名不能为空!!!")

            pic_url_list = list()
            if 'pic-1' in self.request.files and len(self.request.files['pic-1']) > 0:
                res1 = self.request.files['pic-1'][0]
                pic_url_list.append(str(self.goods_ins.store_pic_file(res1['body'])))
            else:
                pic_url_list.append('')
            if 'pic-2' in self.request.files and len(self.request.files['pic-2']) > 0:
                res2 = self.request.files['pic-2'][0]
                pic_url_list.append(str(self.goods_ins.store_pic_file(res2['body'])))
            else:
                pic_url_list.append('')
            if 'pic-3' in self.request.files and len(self.request.files['pic-3']) > 0:
                res3 = self.request.files['pic-3'][0]
                pic_url_list.append(str(self.goods_ins.store_pic_file(res3['body'])))
            else:
                pic_url_list.append('')
            picurls = '|'.join(pic_url_list)

            goods_info = (
                goodsname, price, goodsdesp, time.strftime('%Y-%m-%d'), ret_user['id'], picurls, content, str('ok')
            )
            goods_id = self.goods_ins.create_goods_info(goods_info)
            if not goods_id:
                return self.write("创建商品失败!!!")
            return self.redirect("/goods/view?id=%s" % goods_id)
        elif action == 'view':
            goods_id = self.get_argument('id', None)
            if not goods_id:
                return

            goods_info = self.goods_ins.fetch_goods_info_by_id(goods_id)
            pic_url_list = goods_info['picurls'].split('|')
            if 'pic-1' in self.request.files and len(self.request.files['pic-1']) > 0:
                res1 = self.request.files['pic-1'][0]
                pic_url_list[0] = str(self.goods_ins.store_pic_file(res1['body'], pic_url_list[0] if pic_url_list[0] != '' else None))
            if 'pic-2' in self.request.files and len(self.request.files['pic-2']) > 0:
                res2 = self.request.files['pic-2'][0]
                pic_url_list[1] = str(self.goods_ins.store_pic_file(res2['body'], pic_url_list[1] if pic_url_list[1] != '' else None))
            if 'pic-3' in self.request.files and len(self.request.files['pic-3']) > 0:
                res3 = self.request.files['pic-3'][0]
                pic_url_list[2] = str(self.goods_ins.store_pic_file(res3['body'], pic_url_list[2] if pic_url_list[2] != '' else None))
            picurls = '|'.join(pic_url_list)
            print picurls
            goods_info = (
                goodsname, price, goodsdesp, time.strftime('%Y-%m-%d'), picurls, content
            )
            self.goods_ins.update_goods_info(goods_info)
            return self.redirect("/goods/view?id=%s" % goods_id)


class GoodsStausHandle(BasicHandler):

    @login
    def post(self, action):
        if action == 'active':
            goods_id = self.get_argument("goods_id", None)
            if not goods_id:
                return
            self.goods_ins.set_goods_status_by_id(goods_id, action)
        elif action == 'shield':
            goods_id = self.get_argument("goods_id", None)
            if not goods_id:
                return
            self.goods_ins.set_goods_status_by_id(goods_id, action)
        return


