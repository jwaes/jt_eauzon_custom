
from odoo import api, fields, models, _


class UoM(models.Model):
    _inherit = 'uom.uom'

    code_fragment = fields.Char(string="Code fragment")