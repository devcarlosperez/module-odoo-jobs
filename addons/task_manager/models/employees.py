# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Employee(models.Model):
    _name = 'task_manager.employee'
    _description = 'task_manager.employee'

    name = fields.Char()
    birth_date = fields.Date()
    hire_date = fields.Date()
    country = fields.Many2one("res.country", "Country")
    task_ids = fields.Many2many(
    'task_manager.task',
    'employee_task_rel',
    'employee_id',
    'task_id',
    string="Tasks"
)
    job_position_id = fields.Many2one(
        'jobs.job_position',
        string="Job Position"
    )