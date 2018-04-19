# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
from openerp import models, fields, api


class ConfirmWizard(models.TransientModel):
    _name = 'odoo.confirm.wizard'

    @api.model
    def default_get(self, fields):
        res = super(ConfirmWizard, self).default_get(fields)
        message = self._context.get('message', False)
        res.update({
            'message': message
        })
        return res

    message = fields.Text()

    @api.one
    def execute(self):
        model = self._context.get('model', None)
        record_id = self._context.get('record_id', None)
        method = self._context.get('method', None)
        if model is None or record_id is None or method is None:
            pass
        else:
            getattr(self.env[model].browse(record_id), method)()
