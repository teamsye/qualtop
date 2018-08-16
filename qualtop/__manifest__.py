# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Qualtop App',
    'version': '11.0.1.1.0',
    "author": "Vauxoo",
    "license": "LGPL-3",
    'category': 'Hidden',
    'summary': 'Qualtop App for customizations',
    'depends': [
        'account_accountant',
        'account_cash_basis_base_account',
        'analytic',
        'purchase',
        'sale_management',
    ],
    'data': [
        "data/data.xml",
        "views/account_invoice_view.xml",
        "views/sale_views.xml",
        "views/report_invoice.xml",
        "views/analytic_account_view.xml",
        "data/base_automation_data.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
}
