from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_years_selection():
        year_list = []
        for i in range(2019, 2040):
            year_list.append((i, str(i)))
        return year_list

    service_month = fields.Selection(
        [(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
         (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
         (9, 'September'), (10, 'October'), (11, 'November'),
         (12, 'December'), ], )
    service_year = fields.Selection(_get_years_selection())
