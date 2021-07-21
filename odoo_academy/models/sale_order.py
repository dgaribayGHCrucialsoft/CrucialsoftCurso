# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    session_id=fields.Many2one(comodel_name='academy.session',
                               string='Sesión Relacionada',
                               ondelete='set null')

    instructor_id=fields.Many2one(string='Instructor de la sesión',
                                  related='session_id.instructor_id')
    student_ids=fields.Many2many(string='Estudiantes',
                                 related='session_id.student_ids')