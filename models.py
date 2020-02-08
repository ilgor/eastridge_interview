from datetime import datetime
from config import db, ma


class Invoice(db.Model):
    __name__ = 'invoice'
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