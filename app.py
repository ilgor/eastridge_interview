from datetime import datetime
from flask import request, jsonify
from flask_restful import Api, Resource
from config import app, db
from models import Invoice, InvoiceItem, InvoiceSchema, InvoiceItemSchema


api = Api(app)

class InvoiceListResource(Resource):

    def __init__(self):
        self.invoice_schema = InvoiceSchema(many=True)
    
    def get(self):
        invoices = Invoice.query.all()
        return jsonify(self.invoice_schema.dump(invoices))

    def post(self):
        new_invoice = Invoice(client_name=request.json['client_name'])
        db.session.add(new_invoice)

        for item in request.json['invoice_items']:
            new_invoice_item = InvoiceItem(
                units = item['units'],
                description = item['description'],
                amount = item['amount'],
                invoice = new_invoice
            )
            db.session.add(new_invoice_item)
        db.session.commit()
        return '', 204


class SingleInvoiceListResource(Resource):

    def __init__(self):
        self.invoice_schema = InvoiceSchema()

    def get(self, id):
        invoice = Invoice.query.get_or_404(id)
        return jsonify(self.invoice_schema.dump(invoice))

    def delete(self, id):
        invoice = Invoice.query.get_or_404(id)
        db.session.delete(invoice)
        db.session.commit()
        return '', 204

api.add_resource(InvoiceListResource, '/')
api.add_resource(SingleInvoiceListResource, '/<int:id>')



if __name__ == '__main__':
    app.run(debug=True)