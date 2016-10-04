#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--predict", type=float)
parser.add_argument('--square', type=float)
args = parser.parse_args()

import sklearn.linear_model
import numpy

if args.predict is not None:
    lr = sklearn.linear_model.LinearRegression()
    lr.coef_ = numpy.array([6.0])
    lr.intercept_ = 0.0
    print lr.predict([[args.predict]])
if args.square is not None:
    print args.square**2
