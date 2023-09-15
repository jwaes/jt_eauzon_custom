import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class ProductAttribute(models.Model):
    _inherit = "product.attribute"

    attribute_code = fields.Char(string="Attribute code")    

class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    code_fragment = fields.Char(string="Code fragment")

# class ProductTemplateAttributeValue(models.Model):
#     _inherit = "product.template.attribute.value"

#     color_type = fields.Selection(related="product_attribute_value_id.color_type", readonly=True)
#     css_style = fields.Char(related="product_attribute_value_id.css_style")

#     is_dual = fields.Boolean(compute='_compute_is_dual', string='is_dual')
#     is_css = fields.Char(compute='_compute_is_css', string='is_css')
    
#     @api.depends('color_type')
#     def _compute_is_css(self):
#         for record in self:
#             record.is_css = record.color_type == 'css'
    
#     @api.depends('color_type')
#     def _compute_is_dual(self):
#         for record in self:
#             record.is_dual = record.color_type == 'dual'