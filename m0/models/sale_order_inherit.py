# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrderInherit(models.Model):

    _inherit = 'sale.order'

    extended_field = fields.Selection([('E0', 'Extended option 0'), (
        'E1', 'Extended option 1'), ('E2', 'Extended option 2')], string='EXTENDED')
