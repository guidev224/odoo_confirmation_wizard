# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': "Odoo Confirmation Wizard",

    'summary': """
        """,

    'description': """
    """,

    'author': "BAH Abdourahmane Sank",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Utilities',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'confirm_wizard_view.xml',
    ],
}