# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Ent1(models.Model):
    _name = 'm0.ent1'
    _description = 'Module Template 1'

    name = fields.Char(string="Description")
    bool_white = fields.Boolean(string="Has WHITE", default=True)
    bool_black = fields.Boolean(string="Has BLACK", default=True)



