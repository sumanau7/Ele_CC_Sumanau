from datetime import datetime
from google.appengine.ext import ndb

TxDataType = ['CCBill',
			  'CCVendorPurchase', 
			  'CCVendorPurchase', 
			  'CCOTPMessage', 
			  'CCBillPayment'
			 ]

class CreditCardEvent(ndb.Model):
    """Models an individual CreditCard event entry of different types."""
    type = ndb.StringProperty(choices=TxDataType)
    date_added = ndb.DateTimeProperty(auto_now_add=True)
    date_generated = ndb.DateTimeProperty(default=None)
    cc_number = ndb.IntegerProperty()
    min_due = ndb.FloatProperty(default=0)
    payment_due_date = ndb.DateTimeProperty(auto_now_add=False, default=None)
    total_amount_credited = ndb.FloatProperty(default=0)
    amount_spent = ndb.FloatProperty(default=0)
    available_balance = ndb.FloatProperty(default=0)
    current_outstanding_bill = ndb.FloatProperty(default=0)
    payment_date = ndb.DateTimeProperty(auto_now_add=False, default=None)
    bank_id = ndb.StringProperty(default=None)

# Example of adding Monthly credit card bill notification SMS in NDB Datastore
# cc = CreditCardEvent()
# cc.type = 'CCBill'
# cc.cc_number = 7172
# cc.min_due = 4225.79
# cc.current_outstanding_bill = 17394.86
# cc.payment_due_date = datetime.strptime('17/May/2015', '%d/%b/%Y')
# cc.put()

# Example of adding credit card bill payment in NDB Datastore
# cc = CreditCardEvent()
# cc.type = 'CCBillPayment'
# cc.cc_number = 7172
# cc.total_amount_credited = 17394.86
# cc.payment_date = datetime.now()
# cc.put()

# Example of adding credit card vendor purchase in NDB Datastore
# cc = CreditCardEvent()
# cc.type = 'CCVendorPurchase'
# cc.cc_number = 7172
# cc.amount_spent = 5380.00
# cc.available_balance = 93949.00
# cc.current_outstanding_bill = 6051.00
# cc.put()