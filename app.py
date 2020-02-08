from datetime import datetime
from flask import request, jsonify
from flask_restful import Api, Resource
from config import app, db
from models import Invoice, InvoiceItem, InvoiceSchema, InvoiceItemSchema
import pandas as pd

api = Api(app)


class InvoiceBasedOnAllParamsListResource(Resource):

    def __init__(self):
        self.invoice_schema = InvoiceSchema(many=True)

    def get(self):
        client_name = request.args.get('client_name')
        date_created = request.args.get('date_created')
        units = request.args.get('units')
        description = request.args.get('description')
        amount = request.args.get('amount')

        kwargs_invoice = {}
        kwargs_invoice_item = {}

        if client_name:
            kwargs_invoice['client_name'] = client_name
        if date_created:
            kwargs_invoice['date_created'] = pd.to_datetime(request.args.get('date_created'))
        if units:
            kwargs_invoice_item['units'] = units
        if description:
            kwargs_invoice_item['description'] = description
        if amount:
            kwargs_invoice_item['amount'] = amount
        
        
        result = db.session.query(Invoice)\
            .filter_by(**kwargs_invoice)\
            .join(InvoiceItem)\
            .filter_by(**kwargs_invoice_item)
            
        return jsonify(self.invoice_schema.dump(result))


class InvoiceListResource(Resource):

    def __init__(self):
        self.invoice_schema = InvoiceSchema(many=True)

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


class InvoiceBasedOnClientNameListResource(Resource):

    def __init__(self):
        self.invoice_schema = InvoiceSchema(many=True)

    def get(self, name):
        invoices = Invoice.query.filter_by(client_name=name)
        return jsonify(self.invoice_schema.dump(invoices))

    def delete(self, name):
        invoices = Invoice.query.filter_by(client_name=name)
        for invoice in invoices:
            db.session.delete(invoice)
        db.session.commit()
        return '', 204



api.add_resource(InvoiceBasedOnAllParamsListResource, '/all')
api.add_resource(InvoiceListResource, '/new')
api.add_resource(SingleInvoiceListResource, '/<int:id>')
api.add_resource(InvoiceBasedOnClientNameListResource, '/client/<name>')



if __name__ == '__main__':
    app.run(debug=True)