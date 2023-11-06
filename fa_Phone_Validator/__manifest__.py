# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Phone Number Validater',
    'category': 'Hidden',
    'summary': 'Phone Number Validator',
    'version': '0.1',
    'description': """
    This is a base module. It holds website-related stuff for Contact model (res.partner).
    It check the following in the Phone Number fields. \n
    1. It makes mandatory the Phone Numbers. \n
    2. It provide the Phone number syntax 05XXXXXXXX. \n
    3. It check the phone numbers characters should be 10. \n
    4. IT is as per ksa standard

    More validations will be updated soon. \n
    Fahad Ahmed
    """,
    'depends': ['crm'],
    'data': [

    ],
    'demo': [],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
