# -*- coding: utf-8 -*-

################################################################################
#
#    Copyright (c) 2014 Elastoffice. All rights reserved.
#
################################################################################

from openerp.osv import fields, osv, orm

class eo_ams_category(osv.osv):
    _name = 'eo.ams.category'

    _columns = {
        'name'  : fields.char('Name',size=254,required=True),
        'code'  : fields.char('Code',size=64),
        'note'  : fields.text('Note'),
        'active': fields.boolean('Active'),
    }

    _defaults = {
        'active': 1,
    }   

