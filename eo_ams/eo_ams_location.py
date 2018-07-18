# -*- coding: utf-8 -*-

################################################################################
#
#    Copyright (c) 2014 Elastoffice. All rights reserved.
#
################################################################################

from openerp.osv import fields, osv, orm

class eo_ams_location(osv.osv):
    _name = 'eo.ams.location'

    _columns = {
        'name'      : fields.char('Name',size=254,required=True),
        'site_id'   : fields.many2one('eo.ams.site', 'Site', required=True),
        'asset_ids' : fields.one2many('eo.ams.asset','location_id', string='Assets')
    }



