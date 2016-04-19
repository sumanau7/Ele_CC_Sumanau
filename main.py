# Flask Imports

from flask import Flask, request
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
    response_dict = {}
    # Calculating total min due and total outstanding amount for each card
    for bill in cc_bill:
        cc_number = response_dict.get(bill.cc_number, 0)
        # sum up total min due and total outstanding amount and increase the count to find average.
        if cc_number:
            # { cc_number: (bank_name [0], start_date [1] , due_Date [2] , current_outstanding_bill [3],
            #  total_card_events[4]) }
            response_dict[bill.cc_number] = (bill.bank_id, bill.date_added,\
             + cc_number[2] + bill.current_outstanding_bill, cc_number[3] + 1)
        else:
            # Initially there will no key with cc number
            response_dict[bill.cc_number] = (bill.bank_id, bill.date_added, bill.current_outstanding_bill, 0)
    # Calculating average for min due and total outstanding amount using total instances for that card.
    for cc_number,value in response_dict.iteritems():
        response_dict[cc_number] = (value[0], value[1].strftime('%d'), value[2]/value[3]) 
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

@app.route('/ccDetail')
def cc_detail():
    # Get all CC Bill Statements
    # Breaking expression to improve readibility
    try:
        cc_number = int(request.args.get('cc_number'))
    except:
        return 'Invalid cc'
    cc_bill = CreditCardEvent.query(CreditCardEvent.type=='CCBillPayment', CreditCardEvent.cc_number==cc_number)
    # bank_id, amount_spent, total_amount_credited, payment_due_date, payment_date, penalty
    # sms_transaction  
    cc_bill = cc_bill.fetch(projection=[CreditCardEvent.bank_id, CreditCardEvent.amount_spent, \
        CreditCardEvent.total_amount_credited, CreditCardEvent.payment_due_date, \
        CreditCardEvent.payment_date, \
        CreditCardEvent.late_payment_charges, CreditCardEvent.sms_transaction])
    response_list = []
    for cc in cc_bill:
        bank_id = cc.bank_id,
        amount_spent = cc.amount_spent,
        total_amount_credited = cc.total_amount_credited,
        payment_due_date = cc.payment_due_date.strftime('%d/%b/%Y'),
        payment_date = cc.payment_date.strftime('%d/%b/%Y'),
        delay = (cc.payment_due_date - cc.payment_date).days,
        penalty = cc.late_payment_charges,
        sms_transaction = cc.sms_transaction
        # prepare response list
        response_list.append([bank_id, amount_spent, total_amount_credited,\
         payment_due_date, payment_date, delay, penalty, sms_transaction])
    return json.dumps(response_list)

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
