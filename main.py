# Flask Imports

from flask import Flask
from flask import render_template

# App Imports
from models import CreditCardEvent

# Library Imports
import json
import collections
from datetime import datetime
import datetime as dt

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a base page."""
    return render_template('index.html')


def cc_calculation(cc_bill):
    response_dict = collections.OrderedDict()
    # Calculating total min due and total outstanding amount for each card
    for bill in cc_bill:
        cc_number = response_dict.get(bill.cc_number, 0)
        # sum up total min due and total outstanding amount and increase the count to find average.
        if cc_number:
            # { cc_number: (bank_name [0], start_date [1] , due_Date [2] , min_due [3] , current_outstanding_bill [4],
            #  total_card_events[5]) }
            response_dict[bill.cc_number] = (bill.bank_id, bill.date_added, bill.payment_due_date,\
             cc_number[3] + bill.min_due, cc_number[4] + bill.current_outstanding_bill, \
                cc_number[5] + 1)
        else:
            # Initially there will no key with cc number
            response_dict[bill.cc_number] = (bill.bank_id, bill.date_added, bill.payment_due_date, bill.min_due, bill.current_outstanding_bill, 0)
    # Calculating average for min due and total outstanding amount using total instances for that card.
    for cc_number,value in response_dict.iteritems():
        response_dict[cc_number] = (value[0], value[1].strftime('%d/%b/%Y'), value[2].strftime('%d/%b/%Y'), value[3]/value[5], value[4]/value[5]) 
        return response_dict

@app.route('/ccDetails')
def cc_details():
    # Get CC Bill Statements Notifications
    # Breaking expression to improve readibility
    cc_bill = CreditCardEvent.query(CreditCardEvent.type=='CCBill')
    cc_bill = cc_bill.fetch(projection=[CreditCardEvent.bank_id, CreditCardEvent.date_added, \
        CreditCardEvent.payment_due_date, CreditCardEvent.cc_number, \
        CreditCardEvent.min_due, CreditCardEvent.current_outstanding_bill])
    # Initialize empty dictionary
    response_dict = cc_calculation(cc_bill)
    return json.dumps(response_dict)

@app.route('/ccPaymentCycle')
def cc_payment_cycle():
    cc_bills = CreditCardEvent.query(CreditCardEvent.type=='CCBill')
    response_dict = {}
    for cc_bill in cc_bills:
        cc_payment_log = CreditCardEvent.query(CreditCardEvent.type=='CCBillPayment', \
            CreditCardEvent.total_amount_credited == cc_bill.current_outstanding_bill, CreditCardEvent.payment_date >= cc_bill.date_generated, \
            CreditCardEvent.payment_date <= cc_bill.payment_due_date)
        if cc_payment_log.count() == 0:
            total_bill = cc_bill.current_outstanding_bill
            cc_next_bill = CreditCardEvent.query(CreditCardEvent.type=='CCBillPayment', CreditCardEvent.payment_date > cc_bill.payment_due_date,\
            CreditCardEvent.payment_date < cc_bill.payment_due_date + dt.timedelta(30))
            cc_next_bill = cc_next_bill.fetch(limit=2)
            delay = (cc_next_bill[1].payment_date - cc_bill.payment_due_date).days
            if response_dict.get(cc_bill.cc_number):
            	# Total due, Amount Paid, Payment Due date, Bill generated date, delay
            	response_dict[cc_bill.cc_number].append((cc_bill.current_outstanding_bill, cc_next_bill[0].total_amount_credited, cc_bill.payment_due_date.strftime('%d/%b/%Y'), cc_bill.date_generated.strftime('%d/%b/%Y'), delay))
            else:
            	response_dict[cc_bill.cc_number] = [(cc_bill.current_outstanding_bill, cc_next_bill[0].total_amount_credited, cc_bill.payment_due_date.strftime('%d/%b/%Y'), cc_bill.date_generated.strftime('%d/%b/%Y'), delay)]
    return json.dumps(response_dict)

@app.route('/ccMonthlyPayment')
def cc_monthly_payment():
    cc_bill = CreditCardEvent.query(CreditCardEvent.type=='CCBillPayment').order(CreditCardEvent.payment_date)
    response_dict = collections.OrderedDict()
    sum = 0
    for index,value in enumerate(cc_bill):
        sum = (value.total_amount_credited + sum) if sum else value.total_amount_credited
        response_dict[value.payment_date.strftime('%d/%b/%Y')] = (value.total_amount_credited, sum/(index+1))
    return json.dumps(response_dict)

@app.route('/ccScoreGrid')
def cc_score_grid():
    cc_bill = CreditCardEvent.query(CreditCardEvent.type=='CCBill')    
    response_dict = cc_calculation(cc_bill)
    return json.dumps(response_dict)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
