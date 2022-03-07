# -*- coding: utf-8 -*-
# from odoo import http


# class ConstructionDelivery(http.Controller):
#     @http.route('/construction_delivery/construction_delivery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/construction_delivery/construction_delivery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('construction_delivery.listing', {
#             'root': '/construction_delivery/construction_delivery',
#             'objects': http.request.env['construction_delivery.construction_delivery'].search([]),
#         })

#     @http.route('/construction_delivery/construction_delivery/objects/<model("construction_delivery.construction_delivery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('construction_delivery.object', {
#             'object': obj
#         })
