import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = "product.product"

    def get_attribute_code(self, attribute_code):
        self.ensure_one()
        if attribute_code == "UOM":
            frag = self.uom_id.code_fragment
            if not frag:
                frag = self.uom_id.name.replace(" ", "").upper()
            return frag
        elif attribute_code == "T":
            return str(int(self.thickness))
        elif attribute_code == "D":
            return str(int(self.density))
        else :
            for att_val in self.product_template_variant_value_ids:
                if att_val.attribute_id.attribute_code and att_val.attribute_id.attribute_code == attribute_code:
                    return att_val.product_attribute_value_id.code_fragment
            return None