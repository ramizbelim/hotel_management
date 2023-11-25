# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hotel Management',
    'version' : '16.0.1.0.0',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
Hotel Management
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/account_report.xml',
    ],
    'demo': [
        'demo/account_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
