from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    analytic_tag_ids = fields.Many2many(
        'account.analytic.tag', string='Analytic Tags', copy=False)
    analytic_id = fields.Many2one(
        'account.analytic.account', string='Analytic Account', copy=False)
