# -*- coding: utf-8 -*-

from odoo import models, fields, api

class JobPosition(models.Model):
    _name = 'jobs.job_position'
    _description = 'jobs.job_position'

    name = fields.Char()
    description = fields.Char()
    code = fields.Char()
    estimated_salary = fields.Float()
    start_date = fields.Date()
    job_type = fields.Selection([
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('freelance', 'Freelance'),
        ('intern', 'Intern')])
    department = fields.Many2one("hr.department", "Department")
    category_id = fields.Many2one("jobs.job_category", "Job Category")