
from collections import defaultdict
from odoo import fields, models

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(selection_add=[
            ('2x4', '2 x 4')
        ], ondelete={'2x4': 'set default'})