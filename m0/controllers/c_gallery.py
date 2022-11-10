# -*- coding: utf-8 -*-

import base64
import json
from odoo import http
from odoo.http import request
from odoo.http import Response


class GalleryController(http.Controller):
    # [CONT] REDIRECT TO DISPLAY
    @http.route('/gallery_display', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def gallery_display(self, **kw):
        print("Going to THE GALLERY=======================")
        gallery_requested = http.request.env['m0.photo'].sudo().search([])
        collection = {
            'collection': gallery_requested
        }
        return request.render('m0.gallery_display', collection)
