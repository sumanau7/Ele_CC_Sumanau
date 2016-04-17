# Credit card Bill Payment data

import datetime
import random

list_of_payment = [(640.22,'16/Feb/2016'),
(266.55,'17/Jan/2016'),
(436.95,'18/Dec/2015'),
(553.45,'18/Nov/2015'),
(774.87,'19/Oct/2015'),
(559.35,'19/Sep/2015'),
(728.53,'20/Aug/2015'),
(500.00,'21/Jul/2015'),
(1459.45,'21/Jun/2015'),
(885.97,'22/May/2015'),
(687.02,'22/Apr/2015'),
(932.98,'23/Mar/2015'),
(847.84,'21/Feb/2015'),
(530.96,'22/Jan/2015'),
(849.41,'23/Dec/2014'),
(758.01,'23/Nov/2014'),
(988.67,'24/Oct/2014'),
(999.91,'24/Sep/2014'),
(673.77,'25/Aug/2014'),
(746.36,'26/Jul/2014'),
(464.94,'26/Jun/2014'),
(929.72,'27/May/2014'),
(338.57,'27/Apr/2014'),
(575.27,'28/Mar/2014'),
(600.06,'26/Feb/2014'),
(994.43,'27/Jan/2014'),
(666.67,'28/Dec/2013'),
(344.91,'28/Nov/2013'),
(752.22,'29/Oct/2013'),
(716.15,'29/Sep/2013'),
(274.92,'30/Aug/2013'),
(210.94,'31/Jul/2013'),
(572.57,'01/Jul/2013'),
(726.94,'01/Jun/2013'),
(971.65,'02/May/2013'),
(518.31,'02/Apr/2013'),
(325.36,'03/Mar/2013'),
(524.74,'01/Feb/2013'),
(551.49,'02/Jan/2013'),
(423.23,'03/Dec/2012'),
(637.92,'03/Nov/2012'),
(881.95,'04/Oct/2012'),
(314.37,'04/Sep/2012'),
(554.31,'05/Aug/2012'),
(430.58,'06/Jul/2012'),
(317.05,'06/Jun/2012'),
(862.61,'07/May/2012'),
(198.44,'07/Apr/2012'),
(871.83,'08/Mar/2012'),
(721.66,'07/Feb/2012'),
(647.43,'08/Jan/2012'),
(891.03,'09/Dec/2011'),
(781.53,'09/Nov/2011'),
(703.81,'10/Oct/2011'),
(815.73,'10/Sep/2011'),
(384.08,'11/Aug/2011'),
(866.69,'12/Jul/2011'),
(596.98,'12/Jun/2011'),
(683.14,'13/May/2011'),
(946.86,'13/Apr/2011'),
(105.62,'14/Mar/2011'),
(820.68,'12/Feb/2011'),
(364.36,'13/Jan/2011'),
(868.93,'14/Dec/2010'),
(664.3,'14/Nov/2010'),
(847.84,'15/Oct/2010'),
(804.02,'15/Sep/2010'),
(626.27,'16/Aug/2010'),
(763.29,'17/Jul/2010'),
(722.02,'17/Jun/2010'),
(130.43,'18/May/2010'),
(801.11,'18/Apr/2010'),
(939.29,'19/Mar/2010'),
(638.88,'17/Feb/2010'),
(581.76,'18/Jan/2010'),
(735.3,'19/Dec/2009'),
(944.21,'19/Nov/2009'),
(816.83,'20/Oct/2009'),
(505.06,'20/Sep/2009'),
(822.35,'21/Aug/2009'),
(856.16,'22/Jul/2009'),
(904.33,'22/Jun/2009'),
(625.16,'23/May/2009'),
(865.97,'23/Apr/2009'),
(634.58,'24/Mar/2009'),
(826.29,'22/Feb/2009'),
(282.33,'23/Jan/2009'),
(783.5,'24/Dec/2008'),
(739.65,'24/Nov/2008'),
(949.52,'25/Oct/2008'),
(827.56,'25/Sep/2008'),
(670.75,'26/Aug/2008'),
(798.82,'27/Jul/2008'),
(950.26,'27/Jun/2008'),
(204.99,'28/May/2008'),
(122.51,'28/Apr/2008'),
(861.64,'29/Mar/2008'),
(851.66,'28/Feb/2008'),
(746.14,'29/Jan/2008'),
(987.45,'30/Dec/2007')]

for i in list_of_payment:
    cc = CreditCardEvent()
    cc.type = 'CCBillPayment'
    cc.cc_number = 7172
    cc.total_amount_credited = i[0]
    payment_date = datetime.datetime.strptime(i[1], '%d/%b/%Y')
    payment_date = payment_date + datetime.timedelta(-(random.randint(3,15)))
    cc.payment_date = payment_date
    print cc.put()