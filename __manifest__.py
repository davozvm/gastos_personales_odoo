{
    'name': 'Gastos Personales',
    'version': '1.0',
    'summary': 'Práctica de módulo Odoo para control de gastos',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/gastos_views.xml',
        'views/menus.xml',
    ],
    'application': True,
}