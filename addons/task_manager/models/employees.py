# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Employee(models.Model):
    _name = 'task_manager.employee'
    _description = 'task_manager.employee'

    name = fields.Char()
    birth_date = fields.Date()
    hire_date = fields.Date()
    country = fields.Many2one("res.country", "Country")
    task_ids = fields.Many2many('task_manager.task', 'Tasks')

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100