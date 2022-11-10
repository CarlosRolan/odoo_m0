# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request
import json


class Ent1Controller(http.Controller):
    # TODO CAMBIAR VARIABLES
    # [DESC] REDIRECTS TO A PAGE WHERE ALL ENTITIES OF THE MODEL ENT1 ARE DISPLAYED
    @http.route('/ent1_display', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ent0_display(self, **kw):
        print("Going to DISPLAY [ENT1]=======================")
        ent1_all_requested = http.request.env['m0.ent1'].sudo().search([])
        ent1_all = {
            'ent1_all': ent1_all_requested
        }
        return request.render('m0.ent1_display', ent1_all)
