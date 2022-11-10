# -*- coding: utf-8 -*-
from email.policy import default
from odoo import models, fields, api


class Photo(models.Model):
    _name = 'm0.photo'
    _description = 'Image, a piece of art :"'

    name = fields.Char(string="Name of the artwork")
    on_sale = fields.Boolean(string="On Sale")
    currency = fields.Selection([('€', 'Euros'), ('$', 'Dollar'),
                                ('Rp', 'Riot Points')], string='Currency Type', required=True)
    price = fields.Float(string="Price", default=0)
    image = fields.Binary(string='Source', required=True)

    # RELATIONS
    gallery_ids = fields.Many2many('m0.gallery', string='Galleries')
