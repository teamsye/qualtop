from odoo import models, api


class AccountInvoiceRefund(models.TransientModel):
    _inherit = "account.invoice.refund"

    @api.multi
    def invoice_refund(self):
        res = super(AccountInvoiceRefund, self).invoice_refund()
        data_refund = self.read(['filter_refund'])[0]['filter_refund']
        if data_refund == 'refund' and res.get('domain', False):
            inv_id = self.env.context.get('active_id')
            if not inv_id:
                return res
            inv = self.env['account.invoice'].browse(inv_id)
            """ To obtain the credit note id is necessary search in
            res['domain'] which has the form
            [('type', '=', 'out_refund'), ('id', 'in', [5])]. The credit note
            id is in res['domain'][1][2][0]
            """
            cn_id = [x[2][0] for x in res['domain'] if x[0] == 'id']
            if not cn_id:
                return res
            cn_id = cn_id[0]
            credit_note = self.env['account.invoice'].browse(cn_id)
            credit_note.write({
                'administrative_share': inv.administrative_share,
                'special_share': inv.special_share,
                'concurrent_share': inv.concurrent_share,
                'operative_share': inv.operative_share,
            })
        return res
