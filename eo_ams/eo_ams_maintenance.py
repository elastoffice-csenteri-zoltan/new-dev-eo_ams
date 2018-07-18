# -*- coding: utf-8 -*-

################################################################################
#
#    Copyright (c) 2014 Elastoffice. All rights reserved.
#
################################################################################

from openerp.osv import fields, osv, orm

class eo_ams_site(osv.osv):
    _name = 'eo.ams.maintenance'

    _columns = {
        'name'              : fields.char('Name',size=254,required=True),
        'due_date'          : fields.date('Due Date'),
        'maintenance_by'    : fields.char('Maintenance by', size=128),
        'status'             : fields.selection([
                                ('scheduled','Scheduled'),
                                ('in_progress', 'In progress'),
                                ('on_hold', 'On hold'),
                                ('cancelled', 'Cancelled'),
                                ('completed', 'Completed')],string='Status'),
        'completed_date'    : fields.date('Date completed'),
        'cost_of_repair'    : fields.float('Cost of Repairs'),
        'details'           : fields.text('Description'),
        'asset_id'          : fields.many2one('eo.ams.asset', 'Asset'),

    }

    



