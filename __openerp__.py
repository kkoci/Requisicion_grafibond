##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Requisicion GrafiBond',
    'version': '1',
    'author': 'Kristian Koci',
    'category': 'Compras',
    'images': ['images/purchase_requisitions.jpeg'],
    'website': 'http://www.tuespacioweb.com.ve',
    'description': """
Con este modulo se realizaran las requisiciones en el sistema OpenErp
===========================================================

Por testear con Certificados...
""",
    'depends' : ['compra_grafibond'],
    'demo': ['purchase_requisition_demo.xml'],
    'data': ['security/purchase_tender.xml',
              'wizard/purchase_requisition_partner_view.xml',
              'purchase_requisition_data.xml',
              'purchase_requisition_view.xml',
              'purchase_requisition_report.xml',
              'security/ir.model.access.csv','purchase_requisition_sequence.xml'
    ],
    'auto_install': False,
    'test': [
        'test/purchase_requisition_demo.yml',
        'test/purchase_requisition.yml',
        'test/cancel_purchase_requisition.yml',
    ],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

