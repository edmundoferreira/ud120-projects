#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))





print "#people:",len(enron_data)
print "#features:",len(enron_data["SKILLING JEFFREY K"])

npoi = 0
for person in enron_data:
    if enron_data[person]["poi"] ==1:
        npoi = npoi +1

print "#POI:",npoi


print "\nJames Prentice.total_stock_value:",enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Wesley Colwell.from_this_person_to_poi:",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Jeffery Skilling.exercised_stock_options:",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "\nChairman-Lay.total_payments:",enron_data["LAY KENNETH L"]["total_payments"]
print "CEO-Skilling.total_payments:",enron_data["SKILLING JEFFREY K"]["total_payments"]
print "CFO-Fastow.total_payments:",enron_data["FASTOW ANDREW S"]["total_payments"]


nsal = 0
nemail = 0
ntotalpay = 0
for person in enron_data:
    if not enron_data[person]["salary"]=='NaN':
        nsal = nsal +1
    if not enron_data[person]["email_address"]=='NaN':
        nemail = nemail +1
    if enron_data[person]["total_payments"]=='NaN':
        ntotalpay = ntotalpay +1


print "#salaries:",nsal
print "#emails:",nemail
print "#NaN_total_payments/#people:",ntotalpay/float(len(enron_data))*100



npoi_nan_pay = 0
for person in enron_data:
    if enron_data[person]["poi"] ==1 and enron_data[person]["total_payments"]=='NaN':
        npoi_nan_pay = npoi_nan_pay +1



print "#NaN_poi_total_payments/#poi:",float(npoi_nan_pay)/float(npoi)*100.0
print "#NaN_total_payments+10:",(ntotalpay+10)
