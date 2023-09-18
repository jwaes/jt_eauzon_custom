# -*- coding: utf-8 -*-
{
    'name': "jt_eauzon_custom",

    'summary': "Eauzon backend customizations",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.19',

    # any module necessary for this one to work correctly
    'depends': ['base','web','purchase','stock','sale_management','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/product_product_templates.xml',
        'report/purchase_order_templates.xml',
        'report/purchase_quotation_templates.xml',
        'report/report_invoice.xml',
        'views/fiscal_position.xml',
        'views/product_attribute_views.xml',
        'views/product_template_view.xml',
        'views/report_templates.xml',
        'views/sale_views.xml',
        'views/uom_views.xml',
        'data/report_layout.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],

    'assets': {
        'web.report_assets_common': [
            'jt_eauzon_custom/static/src/scss/layout_eauzon.scss',
        ],
    }
}
