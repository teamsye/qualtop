from odoo import _, api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    l10n_mx_edi_cfdi_second = fields.Binary(
        'CFDI', help='If this invoice was signed with other system, add here '
        'the CFDI to avoid sign the invoice', attachment=True, copy=False)
    l10n_mx_edi_cfdi_second_name = fields.Char(
        'Name of second CFDI', copy=False)
    l10n_mx_edi_comments = fields.Text('Comments', copy=False)

    @api.multi
    def l10n_mx_edi_is_required(self):
        self.ensure_one()
        if self.l10n_mx_edi_cfdi_second:
            return False
        return super().l10n_mx_edi_is_required()

    @api.multi
    def invoice_validate(self):
        result = super(AccountInvoice, self).invoice_validate()
        att_obj = self.env['ir.attachment']
        for inv in self.filtered('l10n_mx_edi_cfdi_second'):
            inv.message_post(_('This CFDI was not signed with Odoo'))
            ctx = self.env.context.copy()
            ctx.pop('default_type', False)
            att_obj.search([('name', '=', inv.l10n_mx_edi_cfdi_second_name),
                            ('res_id', '=', inv.id),
                            ('res_model', '=', inv._name)]).unlink()
            att_obj.with_context(ctx).create({
                'name': inv.l10n_mx_edi_cfdi_second_name,
                'res_id': inv.id,
                'res_model': inv._name,
                'datas': inv.l10n_mx_edi_cfdi_second,
                'datas_fname': inv.l10n_mx_edi_cfdi_second_name,
                'description': 'Mexican invoice',
            })
            inv.l10n_mx_edi_cfdi_name = inv.l10n_mx_edi_cfdi_second_name
        return result
