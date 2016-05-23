#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    #chekcing they all the same size
    import math
    if not (len(predictions) == len(ages) == len(net_worths)):
        print "dataset size mismatch"



    for i in range(0,len(ages)):
        cleaned_data.append((ages[i], net_worths[i], math.pow(net_worths[i]-predictions[i][0],2)))

    orig_size = len(cleaned_data)
    reduction_number = orig_size - int(orig_size*0.9)

    for j in range(0,reduction_number):
        max_i = 0
        max_e = 0
        for i in range(0,len(cleaned_data)):
            if max_e < cleaned_data[i][2]:
                max_e = cleaned_data[i][2]
                max_i = i
        del cleaned_data[max_i]


    if not len(cleaned_data)+reduction_number == orig_size:
        print "size reduction of 90%, missmatch"



    return cleaned_data
