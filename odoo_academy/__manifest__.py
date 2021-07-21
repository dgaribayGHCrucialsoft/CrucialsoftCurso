# -*- coding: utf-8 -*-
{
    'name' : 'odoo Academy',
    'summary' : """Academia. Aplicaciónde entranamiento""",
    'description' :"""
        Academia de cursos
    """,
    'author' : 'Crucialsoft. David Miguel Garibay Rivera.',
    'category' : 'Training',
    'version' : '0.0.1',
    'depends' : ['base','web_cohort','sale'],
    'data' : [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/academy_menuitems.xml',
        'views/css_loader.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
		'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}