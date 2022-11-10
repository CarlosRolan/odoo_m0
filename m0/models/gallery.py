# -*- coding: utf-8 -*-
from email.policy import default
from odoo import models, fields, api


class Gallery(models.Model):
    _name = 'm0.gallery'
    _description = 'Image Gallery with cool styles'

    name = fields.Char(string="Name of the Gallery")

    # RELATIONs
    photo_ids = fields.Many2many('m0.photo', string='Photos presented')

    # COMPUTED
    total_price = fields.Float(string="Total value of the exposition", default=0, compute="_compute_total_value",
                               readonly=True,)

    @api.depends("photo_ids")
    def _compute_total_value(self):
        total_value = 0
        for rec in self:
            for photo in rec.photo_ids:
                total_value = total_value + photo.price

        self.total_price = total_value
