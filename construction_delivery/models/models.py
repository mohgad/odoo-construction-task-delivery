# -*- coding: utf-8 -*-

from odoo import models, fields, api



class construction_delivery(models.Model):
    _name = 'construction_delivery.construction_delivery'
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'construction_delivery.construction_delivery'

    name = fields.Char(string="Name", required=True ,tracking=True)
    users= fields.Many2many('res.users', 'res_users_construction_delivery_rel', 'construction_delivery_id', 'res_users_id', string='Users',tracking=True)
    project=fields.Many2one('project.project','Project',tracking=True)
    task=fields.Many2one('project.task','Task',domain="[('project_id', '=', project)]",tracking=True)
    block_no = fields.Integer(string='Block No.',tracking=True)
    unit_no = fields.Integer(string='Unit No.',tracking=True)
    status= fields.Selection([('rejected','Rejected'),
                              ('accepted','Accepted')],string='Status',tracking=True)
    notes = fields.Text(string='Notes',tracking=True)

    #     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
