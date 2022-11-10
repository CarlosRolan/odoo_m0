# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime


class Ent0(models.Model):
    _name = 'm0.ent0'
    _description = 'Module Template 0'

    name = fields.Char(string="Description")
    customer = fields.Many2one(string="Customer", comodel_name="res.partner")
    date = fields.Datetime(string="Date")
    type = fields.Selection([('T0', 'Type0'), ('T1', 'Type1'),
                            ('T2', 'Type2')], string='Selection type', required=True)
    bool = fields.Boolean(string='Check', default=False)
    image = fields.Binary(string='Image of the Kanban')

    def toggle_state(self):
        self.bool = not self.bool

    # BASIC METHODS=================================================
    # TODO PREGUNTAR POR ESTO
    def refresh(self):
        # This is needed to reload the page after the craton of the new record
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    def f_create(self):
        new_ent0 = {
            'name': 'Auto CREATED entity[type=0]',
            'customer': 1,
            'date': str(datetime.date(2020, 8, 6)),
            'type': 'T0',
            'bool': True,
        }
        print(new_ent0)
        self.env['m0.ent0'].create(new_ent0)
        return self.env['m0.ent0'].refresh()

    def f_update(self):
        print('obj.write()=============================')
        self.write({
            'name': 'auto EDITED entity[type=0]'
        })
        return self.env["m0.ent0"].refresh()

    def f_delete(self):
        print('unlink()=============================')
        self.unlink()
        return self.env["m0.ent0"].refresh()

    # ===============================================================

    # TODO METODO MUY SUICIO que utiliza el prefesional del tutorial pero que NO me gusta
    def f_search_update(self):
        #  metodos y browse se utilizan para lo mismo
        searched_ent0 = self.env['m0.ent0'].search([('name', '=', self.name)])
        print('search()=============================',
              searched_ent0, searched_ent0.name)

        # Con la función browse([0]) seleccionamos el primer resultados que nos devuelve la funcion en
        # en este caso siempre es 1 por eso simpre será la posición [0]
        browsed_ent0 = self.env['m0.ent0'].browse([0])
        print('brose()==============================', browsed_ent0, searched_ent0.name)

        searched_ent0.write({
            'name': 'auto EDITED entity[type=0]'
        })

    def go_to_front(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': '/my/home',
        }


class Ent0Report(models.AbstractModel):

    _name = 'report.m0.report_ent0_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('m0.report_ent0_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['m0.ent0'],
            'docs': self.env['m0.ent0'].browse(docids)
        }

# MarkCALCULTTED FIELD - COMPUTE parameter
# from odoo import api
# total = fields.Float(compute='_compute_total')
# eapi.depends('value', 'tax')
# def_compute_total(self):
# for record in self:
# record.total = record.value+ record.value * record.tax
