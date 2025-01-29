
from odoo import api, fields, models

class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    show_hs_info_on_invoice = fields.Boolean('Show HS Info on invoice', default=False)