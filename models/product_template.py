import logging
import re
from odoo import api, fields, models
from odoo.osv import expression

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = "product.template"

    variant_code_template = fields.Char('Variant code template')

    def generate_variant_codes(self, regenerate=False):
        for tmpl in self:
            _logger.info("Generating variant codes for Product Template '%s'", tmpl.name)
            code_template = tmpl.variant_code_template
            if code_template:
                _logger.info("Code template:[%s]", code_template )
                matches = re.findall("(\$([^\$]*)\$)", code_template)
                if matches :
                    success = True
                    for variant in tmpl.product_variant_ids:
                        result = code_template
                        for match in matches:                            
                            _logger.info("Match %s", match)
                            code_frag = variant.get_attribute_code(match[1])
                            _logger.info("Code frag is '%s'", code_frag)
                            if code_frag == None:
                                success = False
                                _logger.info("Not successfull")
                            elif not code_frag :
                                result = result.replace(match[0], "")
                                _logger.info("Result is empty '%s'", result)
                            else:
                                result = result.replace(match[0], code_frag)
                                _logger.info("Result is '%s'", result)
                        if success:
                            if not variant.default_code or regenerate:
                                variant.default_code = result
                            else:
                                _logger.info("Default code is already set: %s", variant.default_code)


                else :
                    _logger.warn("No matches found") 


            else :
                _logger.info("No code template found for this product template")
