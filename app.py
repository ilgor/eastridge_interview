from datetime import datetime

from flask import request, jsonify
from flask_restful import Api, Resource

from config import app, db
from models import Invoice, InvoiceItem, InvoiceSchema, InvoiceItemSchema


api = Api(app)


class InvoiceListResource(Resource):
    def get(self):
        invoices = Invoice.query.all()
        invoice_schema = InvoiceSchema(many=True)
        return jsonify(invoice_schema.dump(invoices))

    def post(self):
        new_invoice = InvoiceItem(
            client_name=request.json['client_name']
        )
        new_invoice_item = InvoiceItem(
            units = request.json['units'],
            description = request.json['description'],
            amount = request.json['amount'],
            invoice = new_invoice
        )
        db.session.add(new_invoice_item)
        db.session.commit()
        return post_schema.dump(new_invoice_item)

api.add_resource(InvoiceListResource, '/')



if __name__ == '__main__':
    app.run(debug=True)