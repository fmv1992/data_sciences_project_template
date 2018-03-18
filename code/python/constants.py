"""Assign project-wide variables.

Must contain assertions for all the assigned variables (such as paths).

"""
import os

# Cleaning the folders is done by the makefile (not a python function anymore).

ROOT_PATH = '.'
assert os.path.exists(os.path.join(ROOT_PATH, '.git'))

DATA_PATH = os.path.join(ROOT_PATH, 'data')
TMP_PATH = os.path.join(ROOT_PATH, 'tmp')
OUTPUT_PATH = os.path.join(ROOT_PATH, 'output')
PERSITENT_GRID_PATH = os.path.join(OUTPUT_PATH,
                                   'persistent_grid_object.pickle')
assert os.path.exists(DATA_PATH)
assert os.path.exists(TMP_PATH)
assert os.path.exists(OUTPUT_PATH)

_MODELS = [
    # LogisticRegression,
    # DecisionTreeClassifier,
    # GaussianNB,
    # RandomForestClassifier,
    # ExtraTreesClassifier,
    # IsolationForest,
    # XGBClassifier,
    # MLPClassifier,
]


def get_models_instance(): return [x() for x in _MODELS]  # noqa
