from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    create_vendor_reordering_rules = fields.Boolean('Vendor reordering rules', default=False)
    vendor_reordering_route_id = fields.Many2one(
        'stock.location.route', string='Preferred reordering Route', domain="[('product_selectable', '=', True)]")    