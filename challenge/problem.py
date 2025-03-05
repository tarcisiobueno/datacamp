import rampwf as rw
from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd
import numpy as np
import os
import random
random.seed(42)

problem_title = 'Sentiment CLassification with PU Learning'
_prediction_label_names = [0, 1]
_target_column_name = 'label'
_ignore_column_names = []

Predictions = rw.prediction_types.make_multiclass(
    label_names=_prediction_label_names
)

workflow = rw.workflows.Estimator()

score_types = [
    rw.score_types.F1Above(name='F1'), 
    rw.score_types.Accuracy(name='acc'),
]

def get_cv(X, y):
    cv = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
    return cv.split(X, y)

def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, 'data', f_name))
    y_array = data[_target_column_name]
    y_array = np.where(y_array == 2, 1, 0)  # Positive = 1, Unlabeled = 0
    X_df = data.drop([_target_column_name] + _ignore_column_names, axis=1)
    return X_df, y_array

def get_train_data(path='.'):
    f_name = 'train.csv'
    return _read_data(path, f_name)

def get_test_data(path='.'):
    f_name = 'test.csv'
    return _read_data(path, f_name)