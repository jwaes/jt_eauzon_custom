import logging
from odoo.upgrade import util


_logger = logging.getLogger(__name__)


def migrate(cr, version):
    
    modules_to_uninstall = [
        'jt_sale_order_line_codecolumn',
        'jt_invoice_cashdiscount',
        'jt_account_nobanner',
        'excel_import_export',
        'excel_import_export_demo',
        'maintenance_equipment_image',
    ]

    for candidate in modules_to_uninstall:
        _logger.info("About to uninstall module %s", candidate)
        util.uninstall_module(cr,candidate)

    util.remove_view(cr, xml_id='jt_eauzon_custom.report_invoice_document_hs')
    # util.remove_view(cr, xml_id='jt_now_custom.product_quantity')
    # # util.remove_view(cr, xml_id='jt_now_custom.shop_product_carousel_square')

    # util.remove_field(cr, 'mollie.payment.method.issuer', 'payment_icon_ids')
    

