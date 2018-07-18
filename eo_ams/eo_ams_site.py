# -*- coding: utf-8 -*-

################################################################################
#
#    Copyright (c) 2014 Elastoffice. All rights reserved.
#
################################################################################

from openerp.osv import fields, osv, orm

class eo_ams_site(osv.osv):
    _name = 'eo.ams.site'

    _columns = {
        'name'      : fields.char('Name',size=254,required=True),
        'address'   : fields.char('Address',size=254),
        'city'      : fields.char('City', size=128),
        'zip'       : fields.char('Zip',  size=24),
        'state_id'  : fields.many2one('res.country.state', 'State'),
        'country_id': fields.many2one('res.country', 'Country'),
        'description'  : fields.text('Description'),
    }



