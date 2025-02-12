import logging
from odoo.upgrade import util


_logger = logging.getLogger(__name__)


def migrate(cr, version):

    
    modules_to_uninstall = [
        'jt_account_external',
        'jt_account_nobanner',
        'jt_account_sepa',
        'jt_debrand',
        'jt_hr_workday',
        'jt_invoice_cashdiscount',
        'jt_sale_order_line_codecolumn',      
        'jt_mrp_housing',
        'website_hr_recruitment',
    ]

    for candidate in modules_to_uninstall:
        _logger.info("About to uninstall module %s", candidate)
        util.uninstall_module(cr,candidate)    
    
    util.remove_view(cr, xml_id='jt_eauzon_custom.report_purchaseorder_document')