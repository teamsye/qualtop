# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Customizations to EDI mx',
    'version': '11.0.1.0.0',
    "author": "Vauxoo",
    "license": "LGPL-3",
    'category': 'Hidden',
    'summary': 'Mexican Localization for EDI documents qualtop',
    'depends': [
        'l10n_mx_edi',
    ],
    'data': [
        "views/account_invoice_view.xml",
        "views/report_invoice.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
