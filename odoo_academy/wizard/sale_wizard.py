# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleWizard(models.TransientModel):
    _name = 'academy.sale.wizard'
    _description = 'Asistente. Órdenes de venta para las sesiones de estudiantes'

    def _default_session(self):
        return self.env['academy.session'].browse(self._context.get('active_id'))

    session_id=fields.Many2one(comodel_name='academy.session',
                               string='Sesión',
                               required=True,
                               default=_default_session)

    session_student_ids=fields.Many2many(comodel_name='res.partner',
                                         string='Estudiantes en la sesión actual',
                                         related='session_id.student_ids',
										 help='Nombres de los estudiantes que pertenecen a la sesión actual')

    student_ids=fields.Many2many(comodel_name='res.partner', string='Estudiantes de la orden de venta')


    def create_sale_orders(self):
        session_product_id=self.env['product.product'].search([('is_session_product','=',True)], limit=1)
        if session_product_id:
            for student in self.student_ids:
                order_id=self.env['sale.order'].create({
                    'partner_id': student.id,
                    'session_id': self.session_id.id,
                    'order_line': [(0,0, {'product_id': session_product_id.id, 'price_unit': self.session_id.total_price})]
                })