# -*- coding: utf-8 -*-

################################################################################
#
#    Copyright (c) 2014 Elastoffice. All rights reserved.
#
################################################################################

from openerp.osv import fields, osv, orm
import openerp.addons.decimal_precision as dp
import time
from tools.translate import _

class eo_ams_history(osv.osv):
    _name = 'eo_ams.history'

    TYPE =  [
                ('draft', 'Create'),
                ('registration', 'Registration'),
                ('startup', 'Startup'),
                ('revaluation', 'Revaluation'),
                ('revaluation_cancel', 'Revaluation Cancel'),
                ('investment', 'Investment'),
                ('investment_cancel', 'Investment Cancel'),
                ('conservation_start', 'Conservation Start'),
                ('conservation_end', 'Conservation End'),
                ('finished', 'Finished'),
                ('sold', 'Sold'),
                ('depreciation', 'Depreciation'),
                ('scrapped', 'Scrapped'),
                ('duration_change', 'Duration Change'),
                ('conservation_cancel', 'Conservation Cancel'),
                ('out_cancel', 'Cancel Out'),
                ('create_invoice', 'Create Invoice')
            ]

    _columns = {
        'name': fields.char('History name', size=64, select=1),
        'date'      : fields.date(_('Date'),required=True),
        'user_id'           : fields.many2one('res.users', _('User'),required=True),
        'asset_id'          : fields.many2one('eo_asset.asset', _('Asset'),required=True, ondelete='cascade'),
        'type'              : fields.selection( TYPE, _('Type') ),
        # 'value'             : fields.float(_('Value'), digits_compute=dp.get_precision('Account')),
        'note'              : fields.text( _('Note') ),
    
    }
    _order = 'date desc'
    _defaults = {
        'date': lambda *args: time.strftime('%Y-%m-%d'),
        'user_id': lambda self, cr, uid, ctx: uid
    }
