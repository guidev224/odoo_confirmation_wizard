# -*- coding: utf-8 -*-
from openerp import http

class OdooConfirmWizard(http.Controller):
    @http.route('/odoo_confirm_wizard/odoo_confirm_wizard/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/odoo_confirm_wizard/odoo_confirm_wizard/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('odoo_confirm_wizard.listing', {
            'root': '/odoo_confirm_wizard/odoo_confirm_wizard',
            'objects': http.request.env['odoo_confirm_wizard.odoo_confirm_wizard'].search([]),
        })

    @http.route('/odoo_confirm_wizard/odoo_confirm_wizard/objects/<model("odoo_confirm_wizard.odoo_confirm_wizard"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('odoo_confirm_wizard.object', {
            'object': obj
        })