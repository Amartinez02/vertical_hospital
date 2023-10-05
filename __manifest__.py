{
    'name': 'Vertical Hospital',
    'version': '1.0',
    'category': 'Managment',
    'summary': 'Aplicación para vertical de hospitales',
    "depends": ['mail'],
    "author": "Anthony Martinez",
    "license": "LGPL-3",
    "website": "https://www.linkedin.com/in/anthonymartinezestrella/",
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'data/api_rest_setting.xml',
        'views/qs_patients.xml',
        'views/qs_treatments.xml',
        'views/qs_menu.xml',
        'report/qs_patients.xml',
        'views/qs_api_rest.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}