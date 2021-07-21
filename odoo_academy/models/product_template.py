# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_session_product=fields.Boolean(string='Usar como producto de sesión',
                                      help='Chaca esta caja si se trata de un Producto de Sesión',
                                      default=False)