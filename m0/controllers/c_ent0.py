# -*- coding: utf-8 -*-

import base64
import json
from odoo import http
from odoo.http import request
from odoo.http import Response


class Ent0Controller(http.Controller):

    # [CONT] GET THE ENTITIES OF THE MODEL ENT0 IN A JSON
    @http.route('/get_all_ent0', auth='public', method=['GET'], crsf=False)
    def get_all_ent0(self, **kw):
        # VARIANTE search_read([], ['id', 'name', 'bool'])
        try:
            ent0_all_requested = http.request.env['m0.ent0'].sudo().search_read(
                [], ['id', 'name', 'customer', 'type', 'bool'])
            res = json.dumps(ent0_all_requested, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8',
                            status=500)

    # [CONT] REDIRECT TO DISPLAY
    @http.route('/ent0_display', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ent0_display(self, **kw):
        # VARIANT search_read([], ['id', 'name', 'bool'])
        print("Going to DISPLAY ALL [ENT0]=======================")
        ent0_all_requested = http.request.env['m0.ent0'].sudo().search([])
        ent0_all = {
            'ent0_all': ent0_all_requested
        }
        return request.render('m0.ent0_display', ent0_all)

    # [CONT] REDIRECT TO UPDATE FORM
    @http.route('/ent0_update', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ent0_update(self, **kw):
        # VARIANT search_read([], ['id', 'name', 'bool'])
        print("Going to UPDATE [ENT0]=======================")
        ent0_requested = http.request.env['m0.ent0'].sudo().search(
            [('id', '=', kw.get('id'))])
        ent0_to_update = {
            'ent0_to_update': ent0_requested
        }
        return request.render('m0.ent0_update', ent0_to_update)

    # [CONT] ACTION OF UPDATING THE SELECTED RECORD
    @http.route('/ent0_updated', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ent0_updated(self, **kw):
        # i = kw.get('image').stream.read()
        id = int(kw.get('id'))
        print("UPDATING [ENT0]=======================")
        http.request.env['m0.ent0'].sudo().search(
            [('id', '=', id)]).write({
                'name': kw.get('name'),
                # 'customer': kw.get('customer'),
                # 'date': kw.get('date'),
                # 'type': kw.get('type'),
                # 'bool': kw.get('bool'),
                # 'image': base64.encodestring(i),
            }
        )
        return request.redirect('/ent0_display')

    # [CONT] REDIRECTS TO CREATE FORM
    @http.route('/ent0_create', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ent0_create(self, **kw):
        # [IMPORTANT] Here we search for all the clients just to make the user let decide which one to choose as we explained but we use the tag <t-set> instead
        # We use <t-set> instead
        # request0 = http.request.env['res.partner'].sudo().search([])
        # customers = {
        #     'customers': request0
        # }
        print("Going to CREATE [ENT0] form======================")
        return request.render('m0.ent0_create')

    # [CONT] CREATES A NEW RECORD WITH THE VALUES OF THE FORM AND REDIRECTS TO DISPLAY
    @http.route('/ent0_created', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ent0_created(self, **kw):
        if kw['image']:
            i = kw.get('image').stream.read()
        print('=================Creating new Ent0:', kw)
        # First we create the object with the new data
        ent_obj = {
            'name': kw.get('name'),
            'customer': kw.get('customer'),
            'date': kw.get('date'),
            'type': kw.get('type'),
            'bool': kw.get('bool'),
            'image': base64.encodestring(i),
        }
        # Then we insert it into our database
        request.env['m0.ent0'].create(ent_obj)
        # Finally we redirect the user to the route ent0_display
        print("Go to DISPLAY [ENT0]=======================")
        return request.redirect('/ent0_display')

    # [CONT] GOIGN TO DESCRIPTION ACCORDIO
    @http.route('/ent0_description', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ent0_description(self, **kw):
        ent0_obj_requested = request.env['m0.ent0'].sudo().search(
            [('id', '=', kw.get('id'))])
        ent_obj = {
            'ent_obj': ent0_obj_requested
        }
        print('DETAILS OF ========================= ', ent_obj)
        return request.render('m0.ent0_description', ent_obj)

    # [CONT] DELETES THE POINTED RECORD
    @http.route('/ent0_delete', auth='public', type='http', website=True)
    def ent0_delete(self, **kw):
        request.env['m0.ent0'].search([('id', '=', kw.get('id'))]).unlink()
        return request.redirect('/ent0_display')

    @http.route('/ex', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ex(self, **kw):
        id = http.request.env.context.get('uid')
        user_to_edit = request.env['res.users'].sudo().search(
            [('id', '=', id)])

        user = {
            'user': user_to_edit
        }

        print(user_to_edit, "============================")
        return request.render('m0.ex', user)
    # [CONT] UPDATES THE USER IMG FROM THE PORTAL
    @http.route('/ex_update', auth='public', type='http', website=True)
    # ROUTE = FILE.XML NAME
    def ex_update(self, **kw):

        i = kw.get('image_1920').stream.read()

        request.env['res.users'].sudo().search(
            [('id', '=', request.env.context.get('uid'))]).write({
                'image_1920': base64.encodestring(i)})

        return request.redirect('/ex')
