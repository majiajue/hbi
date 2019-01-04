#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import xadmin
from .models import Query
from .actions import generate_report_action

class QueryAdmin(object):
    list_display = ['title', 'description', 'created_by_user', 'sql']
    list_filter = ['title', ]
    raw_id_fields = ['created_by_user', ]

    actions = [generate_report_action()]

xadmin.site.register(Query, QueryAdmin)
