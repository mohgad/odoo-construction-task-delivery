# -*- coding: utf-8 -*-
{
    'name': "Construction Task Delivery",

    'summary': """
       Task Delivery Requests""",

    'description': """
       In construction projects there are 2 groups of users ,first group requests a task delivery with the project and task required and block and unit no.
       the project consists of blocks and each block consist of units ,second group are the approvers who accept or reject the task delivry after inspection 
    """,

    'author': "Mohamed Gad",
    'license':"LGPL-3",
    'website': "mohogad@gmail.com",
    'price':"35.0",
    'currency':"USD",

    'category': 'Project',
    'version': '0.1',

    'depends': ['base',
                'project',
                'mail',
                ],
    'images': ['static/description/cover.png',],

    'data': ['views/views.xml',
             'security/ir.model.access.csv',
             'security/construction_security.xml'

    ],
    'demo': [
    ],
}
