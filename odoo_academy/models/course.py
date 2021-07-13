# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):

    _name = 'academy.course'
    _description = 'Informacion del Curso'

    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')

    level = fields.Selection(string='Nivel',
                             selection=[('begginer','Principiante'),
                                        ('intermediate','Intermedio'),
                                        ('advanced','Avanzado')],
                             copy=False)
							 
    active = fields.Boolean(string='Activo', default=True)