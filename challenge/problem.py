import rampwf as rw
from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd
import os
import random
random.seed(42)

_prediction_label_names = [0, 2]
_target_column_name = 'label'

Predictions = rw.prediction_types.make_multiclass(
    label_names=_prediction_label_names
)

workflow = rw.workflows.Classifier()

scores_types = [
    rw.score_types.F1Above(name='F1'), 
    rw.score_types.Accuracy(name='acc'),
]

def get_cv(X, y):
    cv = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
    return cv.split(X, y)

def _read_data(path, f_name, split_kind, split_test_size):
    data = pd.read_csv(os.path.join(path, 'data', f_name))
    y_array = data[_target_column_name]
    X_df = data.drop([_target_column_name], axis=1)
    testable_indices = data[data[_target_column_name] != 'unlabeled'].index.tolist()
    test_size = int(len(X_df)*split_test_size)
    test_indices = random.sample(testable_indices, test_size)

    if split_kind == 'test':
        X_df = X_df.loc[X_df.index.isin(test_indices)]
        y_array = y_array.loc[y_array.index.isin(test_indices)]
    else:
        X_df = X_df.loc[~X_df.index.isin(test_indices)]
        y_array = y_array.loc[~y_array.index.isin(test_indices)]

    return X_df, y_array

def get_train_data(path='.'):
    f_name = 'final_dataset.csv'
    return _read_data(path, f_name, 'train', 0.4)

def get_test_data(path='.'):
    f_name = 'final_dataset.csv'
    return _read_data(path, f_name, 'test', 0.4)