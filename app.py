from datetime import datetime

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    invoices = db.relationship('InvoiceItem', backref='invoice')


class InvoiceItem(db.Model):
    __name__ = 'invoice_item'
    id = db.Column(db.Integer, primary_key=True)
    units = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(60), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))



class InvoiceItemSchema(ma.ModelSchema):
    class Meta:
        model = InvoiceItem
        exclude = ['id']


class InvoiceSchema(ma.ModelSchema):
    invoices = ma.Nested(InvoiceItemSchema, many=True)
    class Meta: 
        model = Invoice
        exclude = ['id']

invoice_schema = InvoiceSchema(many=True)

class InvoiceListResource(Resource):
    def get(self):
        invoices = Invoice.query.all()
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