# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
{
    'name': "m0",

    'summary': """
      [MODULE 0] Template""",

    'description': """
       This is a template based on the TESTER method of CRD..
    """,

    'author': "CRD",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # We need to ADD SALE_MANAGEMENT for exxtended de wiew of the module Sales
    'depends': ['base', 'sale_management', 'website'],

    # always loaded
    'data': [
        # SECURITY=================================
        'security/ir.model.access.csv',

        # ENT0=================================
        # Views
        'views/ent0/m0_ent0_views.xml',
        # Actions
        'views/ent0/m0_ent0_actions.xml',
        'reports/report_ent0.xml',
        # Front
        'views/ent0/frontend/menu_ent0_website.xml',
        'views/ent0/frontend/ent0_display.xml',
        'views/ent0/frontend/ent0_description.xml',
        'views/ent0/frontend/ent0_create.xml',
        'views/ent0/frontend/ent0_update.xml',

        # ENT1=================================
        # Views
        'views/ent1/m0_ent1_views.xml',
        # Actions
        'views/ent1/m0_ent1_actions.xml',
        # Front
        'views/ent1/frontend/ent1_display.xml',
        'views/ent1/frontend/menu_ent1_website.xml',

        # GALLERY=================================
        'views/gallery/m0_gallery_views.xml',
        'views/gallery/m0_gallery_actions.xml',
        # Front
        'website/pages/menu_gallery_display_website.xml',


        # PHOTO=================================
        # Views
        'views/photo/m0_photo_views.xml',
        # Actions
        'views/photo/m0_photo_actions.xml',
        # Front
        'website/pages/gallery_display.xml',

        # CUSTOM_SALE=================================
        'views/sale_order_inherit/view_extended_form_sales_order.xml',

        # ACCOUNT INHERIT=================================
        'views/portal_inherit/portal_my_details_inherit.xml',
        'views/portal_inherit/portal_my_home_inherit.xml',

        # DASHBOARD INHERIT=================================
        # 'views/dashboard_inherit/dashboard_button_inherit.xml',

        # WEBSITE=================================
        'website/pages/homepage_custom.xml',

        # DASHBOARD=================================
        'views/dashboard_inherit.xml',

        # EXAMPLE=================================
        'views/ent0/frontend/ex.xml',

        # MODULE BACK MENU=================================
        'views/menu_main.xml',

    ],

    # ASSETS
    'assets': {
        'web.assets_frontend': ['m0/static/src/css/m0.css', 'm0/static/src/css/gallery_styles.css'],
        'web.assets_backend': ['m0/static/src/css/m0.css', 'm0/static/src/css/gallery_styles.css']
    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
