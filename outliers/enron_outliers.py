#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]



### your code below
for j in range(0,3):
    max_i = 0
    max_e = 0
    for i in data_dict:
        if max_e < data_dict[i]["salary"] and data_dict[i]["salary"]!='NaN':
            max_e = data_dict[i]["salary"]
            max_i = i

    print "outlier(name,salary):",max_i,max_e
    data_dict.pop(max_i)


data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )





matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
