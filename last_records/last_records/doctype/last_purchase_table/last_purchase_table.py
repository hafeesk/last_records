# -*- coding: utf-8 -*-
# Copyright (c) 2019, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LastPurchaseTable(Document):
	pass

@frappe.whitelist(allow_guest=True)
def getLastprice(item_code, supplier):
	balance_qty = "select prv.name,pitem.item_code,pitem.qty,pitem.rate from `tabPurchase Receipt Item` pitem,`tabPurchase Receipt` prv where pitem.parent = prv.name and pitem.item_code = '"+str(item_code)+"' and prv.supplier = '"+str(supplier)+"' and prv.docstatus != 2 order by prv.creation desc limit 5"
	li=[]
	dic=frappe.db.sql(balance_qty, as_dict=True)
	for i in dic:
		name,item_code,qty,rate=i['name'],i['item_code'],i['qty'],i['rate']
		li.append([name,item_code,qty,rate])
	return li

@frappe.whitelist(allow_guest=True)
def getLastpriceSupplier(item_code):
	balance_qty = "select prv.name,prv.supplier_name,prv.posting_date,pitem.item_code,pitem.qty,pitem.rate from `tabPurchase Receipt Item` pitem,`tabPurchase Receipt` prv where pitem.parent = prv.name and pitem.item_code = '"+str(item_code)+"' and prv.docstatus = 1 order by prv.creation desc limit 3"
	li=[]
	dic=frappe.db.sql(balance_qty, as_dict=True)
	for i in dic:
		name,supplier,posting_date,item_code,qty,rate=i['name'],i['supplier_name'],i['posting_date'],i['item_code'],i['qty'],i['rate']
		li.append([name,supplier,posting_date,item_code,qty,rate])
	return li

@frappe.whitelist(allow_guest=True)
def getLastItempriceSupplier(item_code):
	balance_qty = "select pinv.name,pinv.supplier_name,pinv.posting_date,pitem.item_code,pitem.qty,pitem.rate from `tabPurchase Invoice Item` pitem,`tabPurchase Invoice` pinv where pitem.parent = pinv.name and pitem.item_code = '"+str(item_code)+"' and pinv.docstatus = 1 order by pinv.creation desc limit 3";
	li=[]
	dic=frappe.db.sql(balance_qty, as_dict=True)
	for i in dic:
		name,supplier,posting_date,item_code,qty,rate=i['name'],i['supplier_name'],i['posting_date'],i['item_code'],i['qty'],i['rate']
		li.append([name,supplier,posting_date,item_code,qty,rate])
	return li

@frappe.whitelist(allow_guest=True)
def getLastSalesprice(item_code):
	balance_qty = "select sinv.name,sinv.customer_name,sinv.posting_date,sitem.item_code,sitem.qty,sitem.rate from `tabSales Invoice Item` sitem,`tabSales Invoice` sinv where sitem.parent = sinv.name and sitem.item_code = '"+str(item_code)+"' and sinv.docstatus = 1 order by sinv.creation desc limit 1";
	li=[]
	dic=frappe.db.sql(balance_qty, as_dict=True)
	for i in dic:
		name,customer_name,posting_date,item_code,qty,rate=i['name'],i['customer_name'],i['posting_date'],i['item_code'],i['qty'],i['rate']
		li.append([name,customer_name,posting_date,item_code,qty,rate])
	return li

@frappe.whitelist(allow_guest=True)
def getLastSalespriceCustomer(item_code, customer):
	balance_qty = "select sinv.name,sinv.posting_date,sitem.item_code,sitem.qty,sitem.rate from `tabSales Invoice Item` sitem,`tabSales Invoice` sinv where sitem.parent = sinv.name and sitem.item_code = '"+str(item_code)+"' and sinv.customer = '"+str(customer)+"' and sinv.docstatus = 1 order by sinv.creation desc limit 1";
	li=[]
	dic=frappe.db.sql(balance_qty, as_dict=True)
	for i in dic:
		name,posting_date,item_code,qty,rate=i['name'],i['posting_date'],i['item_code'],i['qty'],i['rate']
		li.append([name,posting_date,item_code,qty,rate])
	return li
