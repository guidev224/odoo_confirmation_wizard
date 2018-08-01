# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
from openerp import models, fields, api, _
# noinspection PyUnresolvedReferences
from openerp.exceptions import except_orm


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
        args = self._context.get('args', False)
        if model is None or record_id is None or method is None:
            pass
        else:
            if not args:
                getattr(self.env[model].browse(record_id), method)()
            else:
                if isinstance(args, dict):
                    getattr(self.env[model].browse(record_id), method)(args)
                else:
                    raise except_orm(_('Error!'), _('The args\' value in the context must be a dictionary!'))

    @api.model
    def show(self, context):
        """
        :param context: a context containing a bunch of information to call
        the method execute.
        Ex.{
                'name': 'Refund Confirmation',
                'model': self._name, <i>Required</i>
                'method': 'method_to_call', <i>Required</i> # Method called when the user hits the yes button
                'record_id': self.id, <i>Required</i>
                'message':'Replace with your custom message' <i>Optional</i> # The default is an empty string
                'args':{'arg1':value1,'arg2':value2,} # Optional dictionary holding the methods arguments
            }
        :return: a action window
        """
        if isinstance(context, dict):
            return {
                'type': 'ir.actions.act_window',
                'name': context.get('name', ''),
                'res_model': 'odoo.confirm.wizard',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'context': context
            }
        else:
            raise except_orm(_('Error!'), _('The context argument must be a dictionary!'))
