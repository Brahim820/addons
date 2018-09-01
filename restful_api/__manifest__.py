{
    'name': 'RESTful API For Odoo',
    'version': '0.0.1',
    'category': 'API',
    'author': 'Babatope Ajepe',
    'website': 'https://ajepe.github.io',
    'summary': 'REST API For Odoo',
    'support': 'galagoapps@gmail.com'
    'description': """
REST API For Odoo
====================
With use of this module user can enable REST API in any Odoo applications/modules

For detailed example of REST API refer *readme.md*
""",
    'depends': [
        'web',
    ],
    'data': [
        'data/ir_config_param.xml',
        'views/ir_model.xml',
        'views/res_users.xml',
        'security/ir_model_access.csv',
    ],
    'images': ['/static/description/icon2.png'],
    'license': 'OPL-1',
    'price': 80.0,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
}
