# -*- coding: utf-8 -*-

################################################################################
#
#   Copyright (c) 2014 Elastoffice. All rights reserved.
#
################################################################################

from openerp.osv import fields, osv, orm
from openerp import SUPERUSER_ID, tools
import logging 

from openerp.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT

LOGGER = logging.getLogger(__name__)

class eo_asset_asset(osv.osv):
    _name = 'eo.ams.asset'

    _inherit = ['mail.thread']
   
    def _get_image(self, cr, uid, ids, name, args, context=None):
        attachment_field = 'image_attachment_id' if name=='image' else 'image_medium_attachment_id'
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = {
                'image': obj.image_attachment_id and obj.image_attachment_id.datas or None,
            }
        return result

    def _set_image(self, cr, uid, id, name, value, args, context=None):
        obj = self.browse(cr, uid, id, context=context)
        image_id = obj.image_attachment_id.id
        
        if not value:
            ids = [attach_id for attach_id in [image_id] if attach_id]
            if ids:
                self.pool['ir.attachment'].unlink(cr, uid, ids, context=context)
            return True
        if not (image_id):
            image_id = self.pool['ir.attachment'].create(cr, uid, {'name': obj.asset_tag_id}, context=context)
            self.write(cr, uid, id, {'image_attachment_id': image_id},context=context)
        
        images = tools.image_get_resized_images(value, return_big=True, avoid_resize_medium=True)
        self.pool['ir.attachment'].write(cr, uid, image_id, {'datas': images['image']}, context=context)
        

        return True

    _columns = {
        'name'              : fields.char('Name', size=256, required=True, select=True, track_visibility='onchange'),
        'purchase_date'     : fields.date(string='Purchase Date',track_visibility='onchange'),
        'purchase_value'    : fields.float(string='Purchase Value', track_visibility='onchange'),
        'currency_id'       : fields.many2one('res.currency', 'Currency', required=True, readonly=True, states={'draft':[('readonly',False)]}, track_visibility='onchange'),
        'asset_tag_id'      : fields.char('Asset Tag ID', size=64, required=True, select=True, track_visibility='onchange'),
        'site_id'           : fields.many2one('eo.ams.site', 'Site', track_visibility='onchange'),
        'location_id'       : fields.many2one('eo.ams.location', 'Location', track_visibility='onchange'),
        'department_id'     : fields.many2one('eo.ams.department', 'Department', track_visibility='onchange'),
        'brand'             : fields.char('Brand', size=64),
        'serial'            : fields.char('Serial no.', size=64),
        'user_id'           : fields.many2one('res.users', 'Assigned to', track_visibility='onchange'),
        'manufacturer_id'   : fields.many2one('res.partner', 'Manufacturer'),
        'vendor_id'         : fields.many2one('res.partner', 'Vendor'),
        'warranty_start'    : fields.date(string='Warranty Start'),
        'warranty_end'      : fields.date(string='Warranty End'),
        'category_id'       : fields.many2one('eo.ams.category', 'Category', track_visibility='onchange'),
        #'event_ids'         : fields.one2many('eo_asset.history', 'asset_id', _('History') ),
        'description'       : fields.text(string='Internal Notes'),
        'state'             : fields.selection([
            ('draft','Draft'),
            ('active', 'Active'),
            ('repair', 'Repair'),
            ('missing', 'Missing'),
            ('scrapped', 'Scrapped')], string='State',track_visibility='onchange', default='active', copy=False),
        'image'             : fields.binary("Image",help="This field holds the image used as image for the asset, limited to 1024x1024px."),
        'active'            : fields.boolean('Active'),
        'maintenance_ids'   : fields.one2many('eo.ams.maintenance','asset_id', string='Maintenances',track_visibility='onchange'),
        'quantity'       : fields.integer(string='Quantity'),


        'image_attachment_id': fields.many2one('ir.attachment', 'Image attachment', help='Technical field to store image in filestore'),
        'image': fields.function(_get_image, fnct_inv=_set_image, string="Image", multi='_get_image', type='binary',
            help="This field holds the image used as image for the product, limited to 1024x1024px."),
      
    }

    def _get_currency(self, cr, uid, context=None):
        res = False

        user = self.pool.get('res.users').browse(cr, uid, [uid])[0]
        if user.company_id:
            company_currency = user.company_id.currency_id.id
        else:
            company_currency = self.pool.get('res.currency').search(cr, uid, [('rate','=',1.0)])[0]
        return company_currency

    _defaults = {
        'active': 1,
        'state' : 'draft',
        'currency_id': _get_currency,
    }

    
