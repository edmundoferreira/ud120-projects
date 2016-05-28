#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score
import numpy as np


# Data Spliting
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)


# Algorithm

clf = DecisionTreeClassifier()
clf.fit(features, labels)

print "#accuracy:",clf.score(features, labels)

clf.fit(features_train, labels_train)

print "#split_accuracy:",clf.score(features_test, labels_test)




print "#POI in test set:",np.sum(labels_test)
print "#test set:",len(labels_test)


labels_pred = clf.predict(features_test)
print "confusion_matrix=",confusion_matrix(labels_test, labels_pred, labels=range(2))


print "precision_score=",precision_score(labels_test, labels_pred)
print "recall_score=",recall_score(labels_test, labels_pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

confmat = confusion_matrix(true_labels, predictions, labels=range(2))
print "confusion_matrix=",confmat

print "TruePositives=",confmat[1][1]
print "TrueNegatives=",confmat[0][0]
print "FalsePositives=",confmat[0][1]
print "FalseNegatives=",confmat[1][0]

print "precision_score=",precision_score(true_labels, predictions)
print "recall_score=",recall_score(true_labels, predictions)
