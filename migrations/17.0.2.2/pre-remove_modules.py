import logging
from odoo.upgrade import util


_logger = logging.getLogger(__name__)


def migrate(cr, version):
    
    modules_to_uninstall = [
        'jt_invoice_cashdiscount',
        'jt_account_nobanner',
        'jt_account_external',
        'jt_debrand',
        'auditlog',
    ]

    for candidate in modules_to_uninstall:
        _logger.info("About to uninstall module %s", candidate)
        util.uninstall_module(cr,candidate)

    util.remove_view(cr, xml_id='jt_debrand.portal_record_sidebar_debrand')
    util.remove_view(cr, xml_id='jt_invoice_cashdiscount.report_invoice_document')
    util.remove_view(cr, xml_id='jt_eauzon_custom.view_order_tree_inherit_eauzon')

    util.remove_view(cr, xml_id='excel_import_export.view_xlsx_template_tree')
    util.remove_view(cr, xml_id='excel_import_export.view_xlsx_template_form')
    util.remove_view(cr, xml_id='excel_import_export.action_xlsx_template')
    # util.remove_view(cr, xml_id='excel_import_export.menu_excel_import_export')
    # util.remove_view(cr, xml_id='excel_import_export.view_xlsx_template_form')            



    # util.remove_view(cr, xml_id='jt_now_custom.product_quantity')
    # # util.remove_view(cr, xml_id='jt_now_custom.shop_product_carousel_square')

    # util.remove_field(cr, 'mollie.payment.method.issuer', 'payment_icon_ids')
    

