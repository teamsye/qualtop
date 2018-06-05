# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    _depends = {
        'account.invoice': [
            'administrative_share', 'special_share', 'concurrent_share',
            'operative_share',
        ],
    }

    administrative = fields.Float(readonly=True)
    special = fields.Float(readonly=True)
    concurrent = fields.Float(readonly=True)
    operative = fields.Float(readonly=True)
    administrative_income = fields.Float(readonly=True)
    special_income = fields.Float(readonly=True)
    concurrent_income = fields.Float(readonly=True)
    operative_income = fields.Float(readonly=True)

    def _select(self):
        res = """,
        administrative_income, special_income, concurrent_income,
        operative_income, administrative, special, concurrent, operative
        """
        return super(AccountInvoiceReport, self)._select() + res

    def _sub_select(self):
        res = """,
        SUM(ail.price_subtotal * invoice_type.sign * ai.administrative_share / 100) AS administrative_income,
        SUM(ail.price_subtotal * invoice_type.sign * ai.special_share / 100) AS special_income,
        SUM(ail.price_subtotal * invoice_type.sign * ai.concurrent_share / 100) AS concurrent_income,
        SUM(ail.price_subtotal * invoice_type.sign * ai.operative_share / 100) AS operative_income,
        SUM(ail.price_total * invoice_type.sign * ai.administrative_share / 100) AS administrative,
        SUM(ail.price_total * invoice_type.sign * ai.special_share / 100) AS special,
        SUM(ail.price_total * invoice_type.sign * ai.concurrent_share / 100) AS concurrent,
        SUM(ail.price_total * invoice_type.sign * ai.operative_share / 100) AS operative
        """
        return super(AccountInvoiceReport, self)._sub_select() + res
