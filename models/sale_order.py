import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amount_to_invoice = fields.Monetary(string="Amount to invoice", store=True, compute='_compute_amount_to_invoice')
    amount_invoiced = fields.Monetary(string="Already invoiced", compute='_compute_amount_invoiced')    

    @api.depends('invoice_ids.state', 'currency_id', 'amount_total')
    def _compute_amount_to_invoice(self):
        for order in self:
            # If the invoice status is 'Fully Invoiced' force the amount to invoice to equal zero and return early.
            if order.invoice_status == 'invoiced':
                order.amount_to_invoice = 0.0
                return

            order.amount_to_invoice = order.amount_total
            for invoice in order.invoice_ids.filtered(lambda x: x.state == 'posted'):
                prices = sum(invoice.line_ids.filtered(lambda x: order in x.sale_line_ids.order_id).mapped('price_total'))
                invoice_amount_currency = invoice.currency_id._convert(
                    prices * -invoice.direction_sign,
                    order.currency_id,
                    invoice.company_id,
                    invoice.date,
                )
                order.amount_to_invoice -= invoice_amount_currency

    @api.depends('amount_total', 'amount_to_invoice')
    def _compute_amount_invoiced(self):
        for order in self:
            order.amount_invoiced = order.amount_total - order.amount_to_invoice    