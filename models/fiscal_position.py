
import json
import logging
import time
from datetime import date, datetime
from odoo import api, fields, models
from odoo.osv import expression
from odoo.tools import date_utils, xlsxwriter, io

_logger = logging.getLogger(__name__)

class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    show_hs_info_on_invoice = fields.Boolean('Show HS Info on invoice', default=False)