# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Qualtop App',
    'version': '11.0.1.0.1',
    "author": "Vauxoo",
    "license": "LGPL-3",
    'category': 'Hidden',
    'summary': 'Qualtop App for customizations',
    'depends': [
        'account_accountant',
        'analytic',
        'purchase',
        'sale_management',
    ],
    'data': [
        "data/data.xml",
        "views/account_invoice_view.xml",
        "views/sale_views.xml",
        "views/report_invoice.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
}
