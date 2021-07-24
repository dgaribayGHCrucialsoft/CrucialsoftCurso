# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):

    _name = 'academy.course'
    _description = 'Informacion del Curso'

    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')

    level = fields.Selection(string='Nivel',
                             selection=[('beginner','Principiante'),
                                        ('intermediate','Intermedio'),
                                        ('advanced','Avanzado')],
                             copy=False)
							 
    active = fields.Boolean(string='Activo', default=True)

    base_price=fields.Float(string="Precio base", default=0.00)
    additional_fee=fields.Float(string="Cuota adicional", default=10.00)
    total_price=fields.Float(string="Precio total", readonly=True)

    foto=fields.Image(string='Fotografía de la Obra')
    archivo=fields.Binary(string='Archivo adjunto')

    session_ids=fields.One2many(comodel_name='academy.session',
                                inverse_name='course_id',
                                string='Sesiones')

    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price<0.00:
            raise UserError(_('El precio base no puede ser negativo'))
        self.total_price = self.base_price + self.additional_fee

    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee<10.00:
                raise ValidationError(_('La cuota adicional no puede ser menor a 10.00: %s'% record.additional_fee))