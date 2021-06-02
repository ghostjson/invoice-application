from openpyxl import Workbook, load_workbook
from database import *
from shutil import copyfile
import json

INVOICE_TEMPLATE = 'resources/templates/invoice.xlsx'
INVOICE_CLIENT = 'B1'
INVOICE_NAME = 'B2'
INVOICE_USER = 'B3'
INVOICE_SMV = 'B4'
INVOICE_LOCATION = 'B5'

INVOICE_ID = 5


INVOICE_ITEM_ID = 'A8'
INVOICE_ITEM_NAME = 'B8'
INVOICE_ITEM_QUANTITY = 'C8'
INVOICE_ITEM_UNIT = 'D8'
INVOICE_ITEM_UNIT_VALUE = 'E8'
INVOICE_ITEM_TOTAL_VALUE = 'F8'

# return total price of an item
def getItemPrice(item_id):

	sqls = ['','', '']

	sqls[0] = "SELECT SUM(price*quantity) AS total_equipment_price FROM Equipments \
		 			INNER JOIN ItemsEquipments \
					ON Equipments.equipment_id = ItemsEquipments.equipment_id \
					WHERE ItemsEquipments.item_id={}".format(item_id)
	sqls[1] = "SELECT SUM(price*quantity) AS total_material_price FROM Materials \
		 			INNER JOIN ItemsMaterials \
					ON Materials.material_id = ItemsMaterials.material_id \
					WHERE ItemsMaterials.item_id={}".format(item_id)
	sqls[2] = "SELECT SUM(hourWage*quantity) AS total_workforce_price FROM WorkForces \
					INNER JOIN ItemsWorkForces \
					ON WorkForces.workForce_id = ItemsWorkForces.workForce_id \
					WHERE ItemsWorkForces.item_id={}".format(item_id)

	total = 0
	for sql in sqls:
		price = list(json.loads(dbGET(sql))[0].values())[0]
		if price != None:
			total += price

	return total

# set invoice sheet
def setInvoiceSheet(invoice_data):

	copyfile(INVOICE_TEMPLATE, 'resources/exports/test.xlsx')

	invoice = load_workbook('resources/exports/test.xlsx')
	invoice_sheet = invoice['invoice']

	invoice_sheet[INVOICE_NAME] = invoice_data['name']
	invoice_sheet[INVOICE_CLIENT] = invoice_data['client']
	invoice_sheet[INVOICE_USER] = invoice_data['user']
	invoice_sheet[INVOICE_SMV] = invoice_data['SMV']
	invoice_sheet[INVOICE_LOCATION] = invoice_data['location']



	invoice_items = invoiceItems(invoice_data['invoice_id'])
	invoice_items_len = len(invoice_items)

	# Entering each item details to the sheet
	for invoice_item in invoice_items:
		invoice_sheet.insert_rows(8)

		invoice_sheet[INVOICE_ITEM_ID] = invoice_item['invoice_id']
		invoice_sheet[INVOICE_ITEM_NAME] = invoice_item['name']
		invoice_sheet[INVOICE_ITEM_QUANTITY] = invoice_item['quantity']
		invoice_sheet[INVOICE_ITEM_UNIT] = invoice_item['unit']
		invoice_sheet[INVOICE_ITEM_UNIT_VALUE] = getItemPrice(invoice_item['item_id'])
		invoice_sheet[INVOICE_ITEM_TOTAL_VALUE] = getItemPrice(invoice_item['item_id']) * float(invoice_item['quantity'])


	INVOICE_SUB_TOTAL = 'F' + str(8+invoice_items_len)
	INVOICE_TAX = 'F' + str(9+invoice_items_len)
	INVOICE_PROFIT = 'F' + str(10+invoice_items_len)
	INVOICE_TOTAL = 'F' + str(11+invoice_items_len)

	# calculate subtotal
	invoice_sheet[INVOICE_SUB_TOTAL] = "=SUM(F8:F{})".format((7+invoice_items_len))
	invoice_sheet[INVOICE_TAX] = "={}*E{}".format(INVOICE_SUB_TOTAL, str(9+invoice_items_len))
	invoice_sheet[INVOICE_PROFIT] = "={}*E{}".format(INVOICE_TAX, str(10+invoice_items_len))
	invoice_sheet[INVOICE_TOTAL] = "=SUM({}:{})".format(INVOICE_SUB_TOTAL, INVOICE_PROFIT)


	invoice.save('resources/exports/test.xlsx')

# return items in a invoice
def invoiceItems(invoice_id):
	query = "SELECT * FROM Items INNER JOIN invoiceItems ON Items.item_id = invoiceItems.item_id WHERE invoiceItems.invoice_id='"+ str(invoice_id) +"'"

	invoice_items = json.loads(dbGET(query))
	return invoice_items

# export function
def export(invoice_id):
	invoices = dbGET('SELECT * FROM Invoices WHERE invoice_id='+ str(invoice_id))
	invoice_data = json.loads(invoices)[0]

	setInvoiceSheet(invoice_data)


if __name__ == '__main__':
	export(INVOICE_ID)
	# getItemPrice(5)
	# invoiceItems(INVOICE_ID)