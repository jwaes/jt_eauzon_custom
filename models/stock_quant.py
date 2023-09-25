
from odoo import api, fields, models, _


class QuantPackage(models.Model):
    _inherit = "stock.quant.package"

    note = fields.Html('Notes')