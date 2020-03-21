# -*- coding: utf-8 -*-
# Copyright (c) 2020, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QuotationTable(Document):
	pass

@frappe.whitelist(allow_guest=True)
def getQuotationprice(item_code, supplier):
	balance_qty = "select qtn.name,qitem.item_code,qitem.qty,qitem.rate from `tabSupplier Quotation Item` qitem,`tabSupplier Quotation` qtn where qitem.parent = qtn.name and qitem.item_code = '"+str(item_code)+"' and qtn.supplier = '"+str(supplier)+"' and qtn.docstatus != 2 order by qitem.rate ASC limit 3"
	li=[]
	dic=frappe.db.sql(balance_qty, as_dict=True)
	for i in dic:
		name,item_code,qty,rate=i['name'],i['item_code'],i['qty'],i['rate']
		li.append([name,item_code,qty,rate])
	return li

@frappe.whitelist(allow_guest=True)
def getQuotationpriceSupplier(item_code):
	balance_qty = "select qtn.name,qtn.supplier_name,qtn.transaction_date,qitem.item_code,qitem.qty,qitem.rate from `tabSupplier Quotation Item` qitem,`tabSupplier Quotation` qtn where qitem.parent = qtn.name and qitem.item_code = '"+str(item_code)+"' and qtn.docstatus = 1 order by qitem.rate ASC limit 3"
	li=[]
	dic=frappe.db.sql(balance_qty, as_dict=True)
	for i in dic:
		name,supplier,posting_date,item_code,qty,rate=i['name'],i['supplier_name'],i['transaction_date'],i['item_code'],i['qty'],i['rate']
		li.append([name,supplier,posting_date,item_code,qty,rate])
	return li