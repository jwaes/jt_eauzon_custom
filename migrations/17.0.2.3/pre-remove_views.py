import logging
from odoo.upgrade import util


_logger = logging.getLogger(__name__)


def migrate(cr, version):
    
    util.remove_view(cr, xml_id='jt_eauzon_custom.report_simple_label2x4')
    util.remove_view(cr, xml_id='jt_eauzon_custom.report_productlabel')    


