# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'task_manager.task'
    _description = 'task_manager.task'

    name = fields.Char()
    description = fields.Char()
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta')])
    deadline = fields.Date()
    employee_ids = fields.Many2many(
    'task_manager.employee',
    'employee_task_rel',
    'task_id',
    'employee_id',
    string="Employees"
)
