# -*- coding: utf-8 -*-
################################################################################
#
#    Copyright (c) 2014 Elastoffice. All rights reserved.
#
################################################################################

{
    'name': 'Asset Management System – developed by Elastoffice',
    'version': '1.0',
    'category': 'Account',
    'summary': 'Asset Management System functions.',
    'description': """
EO ASM
==================================================
Asset management functions.
    """,
    'author': 'Elastoffice',
    'website': 'http://www.elastoffice.com',
    'depends': ['base','mail'],
    'data': [
                'eo_ams_category_view.xml',
                'eo_ams_asset_view.xml',
                'eo_ams_site_view.xml',
                'eo_ams_location_view.xml',
                'eo_ams_department_view.xml',
                'eo_ams_users_view.xml',
                'eo_ams_maintenance_view.xml',
                'menus.xml',
            ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'Other proprietary'
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
