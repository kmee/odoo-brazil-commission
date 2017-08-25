# -*- coding: utf-8 -*-
# © 2017 KMEE INFORMATICA LTDA (https://www.kmee.com.br)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'L10n BR Sale Commission',
    'summary': """L10n BR Sale Commission""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'KMEE,Odoo Community Association (OCA)',
    'website': 'www.kmee.com.br',
    'depends': [
        'l10n_br_base',
        'sped_sale',
        'sale_commission',
    ],
    'data': [
        # 'view/account_invoice_view.xml',
        'view/sale_order_view.xml',
        'view/sale_order_line_view.xml',
        'view/sped_participante.xml',
        # 'report/settlements_report.xml',
    ],
    'demo': [
        'demo/commission_demo.xml'
    ],
    'installable': True,
}
