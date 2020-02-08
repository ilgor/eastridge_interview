import os
from config import db
from models import Invoice, InvoiceItem

INVOICES = [
    {'client_name': 'Eastridge', 'invoice_items': [{'units': 5, 'description': 'Some cool product #1', 'amount': 19.99}, {'units': 10, 'description': 'Some cool product #2', 'amount': 29.99}]},
    {'client_name': 'Ilgor', 'invoice_items': [{'units': 20, 'description': 'Some cool product', 'amount': 39.99}]}
]

if os.path.exists("invoices.db"):
    os.remove("invoices.db")

db.create_all()

for invoice in INVOICES:
    i = Invoice(client_name=invoice['client_name'])
    for item in invoice['invoice_items']:
        ii = InvoiceItem(units=item['units'], description=item['description'], amount=item['amount'], invoice=i)
        db.session.add(ii)
    db.session.add(i)

db.session.commit()