from odoo import api, fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom'
    
    @api.constrains('operation_ids', 'byproduct_ids', 'type')
    def _check_subcontracting_no_operation(self):
        # if self.filtered_domain([('type', '=', 'subcontract'), '|', ('operation_ids', '!=', False), ('byproduct_ids', '!=', False)]):
        #     raise ValidationError(_('You can not set a Bill of Material with operations or by-product line as subcontracting.'))    
        return True