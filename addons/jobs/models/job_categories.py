# -*- coding: utf-8 -*-

from odoo import models, fields, api

class JobCategory(models.Model):
    _name = 'jobs.job_category'
    _description = 'jobs.job_category'

    name = fields.Char()
    description = fields.Char()
    code = fields.Char()
    job_position_ids = fields.One2many('jobs.job_position', 'category_id', "Job Positions")