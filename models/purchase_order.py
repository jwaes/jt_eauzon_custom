import logging
import re
from odoo import api, fields, models, SUPERUSER_ID
from odoo.osv import expression

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _create_orderpoints(self):
        _logger.info("Creating order points")
        for po in self:
            _logger.info("PO %s", po)
            if po.partner_id.create_vendor_reordering_rules:
                partner = po.partner_id
                for line in po.order_line:
                    if not line.display_type:
                        if line.product_id.type == 'product':
                            product = line.product_id
                            location = partner.property_stock_supplier
                            if location.usage == 'internal':
                                if not line.product_id.orderpoint_ids.filtered(lambda o: o.location_id == location):
                                    _logger.info("About to create orderpoint")
                                    orderpoint_values = self.env['stock.warehouse.orderpoint']._get_orderpoint_values(product.id, location.id)
                                    orderpoint_values.update({
                                        # 'name': _('Replenishment Report'),
                                        # # 'warehouse_id': location.warehouse_id.id or self.env['stock.warehouse'].search([('company_id', '=', location.company_id.id)], limit=1).id,
                                        # 'company_id': location.company_id.id,                                    
                                        'route_id': partner.vendor_reordering_route_id.id,
                                    })                                    
                                    _logger.info("Creating orderpoint with values: %s", orderpoint_values)
                                    orderpoint = self.env['stock.warehouse.orderpoint'].with_user(SUPERUSER_ID).create(orderpoint_values)                                                 

            else:
                _logger.info("Nothing to do for this vendor")
                