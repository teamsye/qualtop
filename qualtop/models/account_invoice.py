from odoo import fields, models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    approved_payment = fields.Boolean(copy=False, default=False)

    @api.multi
    def approve_payment_on_invoices(self):
        for invoice in self.filtered(lambda x: x.state == 'open'):
            invoice.approved_payment = True

    @api.multi
    def disapprove_payment_on_invoices(self):
        for invoice in self.filtered(lambda x: x.state == 'open'):
            invoice.approved_payment = False
