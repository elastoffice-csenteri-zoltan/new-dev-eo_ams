# -*- coding: utf-8 -*-
################################################################################
#
#    Copyright (c) 2012 Elastoffice. All rights reserved.
#
################################################################################

from openerp.osv import osv, fields

class res_users(osv.osv):
    
    _name = "res.users"
    _inherit = "res.users"

    _columns = {
        'site_id'           : fields.many2one('eo.ams.site', 'Site', track_visibility='onchange'),
        'location_id'       : fields.many2one('eo.ams.location', 'Location', track_visibility='onchange'),
        'department_id'     : fields.many2one('eo.ams.department', 'Department', track_visibility='onchange'),
        'asset_ids'         : fields.one2many('eo.ams.asset','location_id', string='Assets')
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: