#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "HBI数据平台"
    site_footer = "同程艺龙"
    menu_style = "accordion"

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)