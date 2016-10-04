#!/usr/bin/env python
import sklearn.linear_model
import numpy
import json

lr = sklearn.linear_model.LinearRegression()

params = json.loads(open('lr.json').read())
if params['regressor'] != 'linear':
    print "Mismatch between model and program"
else:
    lr.coef_ = numpy.array(params['coefficients'])
    lr.intercept_ = params['intercept']
    print lr.predict([[1.5]])
