{
    'name': 'Estate',
    'author': 'Bakari Bubu',
    'website': 'https://github.com/BAKARIBUBU',
    'summary': 'estate management',
    'version': '1.0',
    'category': 'Real Estate',
    'description': 'Customize Estate Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_menu.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_type_menu.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_tag_menu.xml',
        'views/estate_property_offer_views.xml'
    ],
    'demo': [],
    'license': 'LGPL-3',  # adding a report to the module
    'installable': True,
    'application': True,
    'auto_install': False,
    "images": ["static/description/icon.png"],
}