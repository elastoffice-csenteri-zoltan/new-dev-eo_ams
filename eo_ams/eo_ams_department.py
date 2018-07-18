# -*- coding: utf-8 -*-

################################################################################
#
#    Copyright (c) 2014 Elastoffice. All rights reserved.
#
################################################################################

from openerp.osv import fields, osv, orm

class eo_ams_location(osv.osv):
    _name = 'eo.ams.department'

    _columns = {
        'name'      : fields.char('Name',size=254,required=True),
    }



