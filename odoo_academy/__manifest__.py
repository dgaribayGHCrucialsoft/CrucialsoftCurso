# -*- coding: utf-8 -*-
{
    'name' : 'odoo Academy',
    'summary' : """Academy app training""",
    'description' :"""
        Academy curses
    """,
    'author' : 'crucialsoft',
    'category' : 'Training',
    'version' : '0.0.1',
    'depends' : ['base'],
    'data' : [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}