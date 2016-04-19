import re

from datetime import datetime
import random
from google.appengine.ext import ndb

data = [{'datetime': '2016-02-04 13:42:17 GMT+05:30',
  'id': 23,
  'mms': False,
  'number': 'DM-DOMINO',
  'sender': False,
  'text': 'Now order ur fav DOMINOS PIZZA from our new outlet at Ashok Nagar, Udaipur. Walk in & Enjoy inaugural offer 25%off. Min bill Rs.350. Cpn: AL25A. Vld:7Feb. T&C',
  'timestamp': 1454573537324},
 {'datetime': '2016-02-03 13:25:37 GMT+05:30',
  'id': 14,
  'mms': False,
  'number': 'AM-VRFSMS',
  'sender': False,
  'text': 'Microsoft account single-use code: 3852297',
  'timestamp': 1454486137185},
 {'datetime': '2016-02-03 12:06:48 GMT+05:30',
  'id': 13,
  'mms': False,
  'number': 'YR-MTSSER',
  'sender': False,
  'text': 'Aavashyak Suchna-Aaj Aapke MTS No.8104159127 ki Due Date Hai Turant Rs.802 Ka Bhugtan Kare or Nirantar Sevao Ka Labh Uthaye.',
  'timestamp': 1454481408330},
 {'datetime': '2016-02-02 10:38:09 GMT+05:30',
  'id': 6,
  'mms': False,
  'number': 'DM-DOMINO',
  'sender': False,
  'text': "It's time to indulge again with Domino's Pizza;Get Garlic Bread &Dip FREE on Min Bill of 399.Call 18602008888.Cpn: MOB04. Vld:11Feb.T&C",
  'timestamp': 1454389689652},
 {'datetime': '2016-02-02 00:23:49 GMT+05:30',
  'id': 1,
  'mms': False,
  'number': 'TD-INNSET',
  'sender': False,
  'text': 'Hi! Pls insert Tata Docomo SIM in slot 1 to enjoy Fast internet Speed. Data usage without pack will be charged \xc2\xbf base rates.',
  'timestamp': 1454352829541},
 {'datetime': '2016-01-01 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Your State Bank of India - visa credit card number 5105105105105100 has been successfully activated. Your card is valid upto 10/11/2020',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-01 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Your ICICI - credit card number 5555555555554444 (Master card) has been successfully activated. Your card is valid upto 12/12/2019',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-01 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Your Central Bank of India - visa credit card number 4012888888881881 has been successfully activated. Your card is valid upto 8/12/2021',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-08 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 350.13 on 8/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-15 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 15120.78 on 15/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-23 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 10120.28 on 23/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-28 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Your SBI card number ending in 5100 has a bill amount of INR 25591.19 for month january ,your due date is 30/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-05 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 5100 of Rs. 25591.19 for january month . Your due date was 30/1/2016 . Your payment has been made on 2/2/2016 . Late payment charges Rs. 300.00 ',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-10 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 500.00 on 10/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-17 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 10050.78 on 17/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-21 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 10120.28 on 21/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-26 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Your ICICI card number ending in 4444 has a bill amount of INR 20671.06 for month january ,your due date is 29/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-01 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 4444 of Rs. 20671.06 for january month . Your due date was 29/1/2016 . Your payment has been made on 1/2/2016 . Late payment charges Rs. 500.00 ',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-09 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 700.00 on 9/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-17 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 2000.00 on 17/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-21 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 3000.00 on 21/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-28 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Your ICICI card number ending in 1881 has a bill amount of INR 5700.00 for month january ,your due date is 30/1/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-31 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 1881 of Rs. 5700.00 for january month . Your due date was 30/1/2016 . Your payment has been made on 1/2/2016 . Late payment charges Rs. 100.00 ',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-08 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 1000.00 on 8/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-13 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 2000.00 on 13/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-19 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 7000.00 on 19/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-28 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Your ICICI card number ending in 5100 has a bill amount of INR 10000.00 for month march ,your due date is 28/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-05 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 5100 of Rs. 10000.00 for january march . Your due date was 28/2/2016 . Your payment has been made on 1/3/2016 . Late payment charges Rs. 200.00 ',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-10 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 1500.00 on 10/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-17 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 2500.00 on 17/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-21 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 1000.00 on 21/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-26 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Your ICICI card number ending in 4444 has a bill amount of INR 5000.00 for month febrary ,your due date is 29/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-29 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 4444 of Rs. 5000.00 for january month . Your due date was 29/2/2016 . Your payment has been made on 29/2/2016 . Late payment charges Rs. 0.00 ',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-09 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 1700.00 on 9/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-17 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 3000.00 on 17/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-21 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 13000.00 on 21/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-02-28 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Your ICICI card number ending in 1881 has a bill amount of INR 3300.00 for month febrary ,your due date is 28/2/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-01-31 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 1881 of Rs. 3300.00 for january month . Your due date was 28/2/2016 . Your payment has been made on 28/2/2016 . Late payment charges Rs. 0.00 ',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-10 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 6000.00 on 10/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-13 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 10000.00 on 13/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-17 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 5100 for payment of INR 7000.00 on 17/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-28 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'Your ICICI card number ending in 5100 has a bill amount of INR 23000.00 for month march ,your due date is 30/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-30 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'AM-SBICAR',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 5100 of Rs. 23000.00 for march . Your due date was 30/3/2016 . Your payment has been made on 30/3/2016 . Late payment charges Rs. 0.00 ',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-14 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 3400.00 on 14/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-21 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 2500.00 on 21/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-22 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 4444 for payment of INR 1000.00 on 22/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-26 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'Your ICICI card number ending in 4444 has a bill amount of INR 6900.00 for month march ,your due date is 29/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-29 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'ICICI-CREDIT',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 4444 of Rs. 6900.00 for march month . Your due date was 29/3/2016 . Your payment has been made on 29/3/2016 . Late payment charges Rs. 0.00 ',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-12 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 1500.00 on 12/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-17 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 3000.00 on 17/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-24 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Thank you for using your credit card ending with 1881 for payment of INR 1000.00 on 24/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-28 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'Your ICICI card number ending in 1881 has a bill amount of INR 4500.00 for month febrary ,your due date is 31/3/2016',
  'timestamp': 1459422293937},
 {'datetime': '2016-03-31 16:34:53 GMT+05:30',
  'id': 370,
  'mms': False,
  'number': 'CENT-CREDIT',
  'sender': False,
  'text': 'We confirm your bill payment for card number ending with 1881 of Rs. 4500.00 for january month . Your due date was 31/3/2016 . Your payment has been made on 31/3/2016 . Late payment charges Rs. 0.00 ',
  'timestamp': 1459422293937}]


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
    late_payment_charges = ndb.FloatProperty(default=0)
    sms_transaction = ndb.StringProperty()

positive_words = ['card','credit','due date']
negative_words = ['Thank you']
neutral_words = ['ending']

for datum in data:
    positive_affinity = 0
    negative_affinity = 0
    neutral_affinity = 0
    for p in positive_words:
        if p in datum['text']:
            positive_affinity = positive_affinity+1
    for n in negative_words:
        if n in datum['text']:
            negative_affinity = negative_affinity+1
    for nw in neutral_words:
        if nw in datum['text']:
            neutral_affinity = neutral_affinity+1
    if neutral_affinity:
        postive_affinity = positive_affinity + neutral_affinity
        negative_affinity = negative_affinity + neutral_affinity
    if positive_affinity and positive_affinity > negative_affinity:
        # find if its bill generation message or bill payment message
        bill_generation_message = re.findall(".*ending in (\d+).* (\d+.\d+).*due date.* (\d+\/\d+\/\d+)",\
            datum['text'])
        bill_payment_message = re.findall(".*bill payment.*ending with (\d+).* (\d+.\d+).*due date was (\d+\/\d+\/\d+).*Your payment.* (\d+\/\d+\/\d+).*Late payment charges.* (\d+.\d+)",\
            datum['text'])
        if bill_generation_message:
            # print 'bill_generation_message'
            # Card Number, Total Amount, Due Date
            # print bill_generation_message
            cc = CreditCardEvent()
            cc.type = 'CCBill'
            cc.cc_number = int(bill_generation_message[0][0])
            cc.current_outstanding_bill = float(bill_generation_message[0][1])
            cc.payment_due_date = datetime.strptime(bill_generation_message[0][2], '%d/%m/%Y')
            cc.sms_transaction = datum['text']
            cc.bank_id = datum['number'].split('-')[1]
            print datum['number'].split('-')[1]
            cc.put()

        if bill_payment_message:
            # print 'bill_payment_message'
            # Card Number, Amount Paid, due date, payment date, late payment charges
            # print bill_payment_message
            cc = CreditCardEvent()
            cc.type = 'CCBillPayment'
            cc.cc_number = int(bill_payment_message[0][0])
            cc.total_amount_credited = float(bill_payment_message[0][1])
            cc.payment_due_date = datetime.strptime(bill_payment_message[0][2], '%d/%m/%Y')
            cc.payment_date = datetime.strptime(bill_payment_message[0][3], '%d/%m/%Y')
            cc.late_payment_charges = float(bill_payment_message[0][4])
            cc.sms_transaction = datum['text']
            cc.bank_id = datum['number'].split('-')[1]
            cc.put()