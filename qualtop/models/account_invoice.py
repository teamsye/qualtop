from odoo import fields, models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.one
    @api.depends('administrative_share', 'special_share', 'concurrent_share',
                 'operative_share', 'state', 'amount_untaxed', 'amount_total')
    def _compute_share(self):
        rround = lambda val: self.currency_id.round(
            self.amount_untaxed * val / 100)
        cround = lambda val: self.currency_id.round(
            self.amount_total * val / 100)
        self.administrative_income = rround(self.administrative_share)
        self.special_income = rround(self.special_share)
        self.concurrent_income = rround(self.concurrent_share)
        self.operative_income = rround(self.operative_share)
        self.administrative = cround(self.administrative_share)
        self.special = cround(self.special_share)
        self.concurrent = cround(self.concurrent_share)
        self.operative = cround(self.operative_share)

    approved_payment = fields.Boolean(copy=False, default=False)
    administrative_income = fields.Monetary(
        copy=False, readonly=True, currency_field='currency_id', store=True,
        compute='_compute_share')
    special_income = fields.Monetary(
        copy=False, readonly=True, currency_field='currency_id', store=True,
        compute='_compute_share')
    concurrent_income = fields.Monetary(
        copy=False, readonly=True, currency_field='currency_id', store=True,
        compute='_compute_share')
    operative_income = fields.Monetary(
        copy=False, readonly=True, currency_field='currency_id', store=True,
        compute='_compute_share')
    administrative = fields.Monetary(
        copy=False, readonly=True, currency_field='currency_id', store=True,
        compute='_compute_share')
    special = fields.Monetary(
        copy=False, readonly=True, currency_field='currency_id', store=True,
        compute='_compute_share')
    concurrent = fields.Monetary(
        copy=False, readonly=True, currency_field='currency_id', store=True,
        compute='_compute_share')
    operative = fields.Monetary(
        copy=False, readonly=True, currency_field='currency_id', store=True,
        compute='_compute_share')
    administrative_share = fields.Float(copy=False)
    special_share = fields.Float(copy=False)
    concurrent_share = fields.Float(copy=False)
    operative_share = fields.Float(copy=False)

    _sql_constraints = [
        ('global_sum', 'CHECK (administrative_share+special_share+concurrent_share+operative_share<=100)', 'Wrong Distribution Shares !'),  # noqa
        ('positive_share', 'CHECK (administrative_share>=0 AND special_share>=0 AND concurrent_share>=0 AND operative_share>=0)', 'All Distribution must positive numbers !'),  # noqa
    ]

    @api.multi
    def approve_payment_on_invoices(self):
        for invoice in self.filtered(lambda x: x.state == 'open'):
            invoice.approved_payment = True

    @api.multi
    def disapprove_payment_on_invoices(self):
        for invoice in self.filtered(lambda x: x.state == 'open'):
            invoice.approved_payment = False
