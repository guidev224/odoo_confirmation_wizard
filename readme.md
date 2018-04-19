## Odoo Confirmation Wizard
This module allows you to add a confirmation step to you business logic.
You can customize the message you want to display.
You can achieve that by following these 3 steps:
1. Add the odoo_confirm_wizard to your module's dependencies
2. Return a window action from anywhere in your code.

## Example
```python
return {
    'type': 'ir.actions.act_window',
    'name': 'The name of the action',
    'res_model': 'odoo.confirm.wizard',
    'view_type': 'form',
    'view_mode': 'form',
    'target': 'new',
    'context': {
        'model': self._name, # Required
        'method': 'method_to_call', # Required Method called when the user hits the yes button
        'record_id': self.id, # Required
        'message':'Replace with your custom message' # Optional The default is an empty string
    }
}
```
3. Define the method to call in the model you have indicated

## Limitation
When the method you want to call returns an action (eg. window action) it is not triggered.

## Contribution
Fell free to enrich this module with your briliant ideas

<!---(Fork me on [Github](https://github.com/guidev224/odoo_confirmation_wizard))--->
