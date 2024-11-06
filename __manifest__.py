# purchase_issue_tracker/__manifest__.py
{
    'name': 'Purchase Issue Tracker',
    'version': '1.0',
    'summary': 'Track issues with purchased products',
    'description': 'Module to track issues with purchase orders and products from vendors.',
    'author': 'Anand VM',
    'company': 'CatalistERP',
    'website': 'https://www.catalisterp.com/',
    'category': 'Purchases',
    'depends': ['base', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/issue_tracker_view.xml',
        'views/menu.xml',
    ],
    # 'images': ['static/description/icon.png'],
    'images': ['static/description/icon.png', 'static/description/screenshot1.png', 'static/description/screenshot2.png'],
    'installable': True,
    'application': True,
}
