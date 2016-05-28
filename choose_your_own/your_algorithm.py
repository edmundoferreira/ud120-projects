#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier



gnb_clf = GaussianNB()
gnb_clf.fit(features_train, labels_train)
print "#GaussianNaiveBayes_score:",gnb_clf.score(features_test, labels_test)

dt_clf = DecisionTreeClassifier()
dt_clf.fit(features_train, labels_train)
print "#DecisionTree_score:",dt_clf.score(features_test, labels_test)


svm_clf = SVC()
svm_clf.fit(features_train, labels_train)
print "#SVM_score:",svm_clf.score(features_test, labels_test)


knn_clf = KNeighborsClassifier(n_neighbors=1)
knn_clf.fit(features_train, labels_train)
print "#kNN_score:",knn_clf.score(features_test, labels_test)


ada_clf = AdaBoostClassifier()
ada_clf.fit(features_train, labels_train)
print "#AdaBoost_score:",ada_clf.score(features_test, labels_test)


rf_clf = RandomForestClassifier()
rf_clf.fit(features_train, labels_train)
print "#RandomForest_score:",rf_clf.score(features_test, labels_test)





clf = knn_clf



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
