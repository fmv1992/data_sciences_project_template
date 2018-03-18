"""Grids for grid search."""

import numpy as np

_XGBOOST_GRID = {
    'colsample_bytree': [0.8],
    'colsample_bylevel': [0.8],
    'reg_lambda': [0.5, 1, 5],
    'reg_alpha': [0, 0.1, 0.5],
    'gamma': [0, ] + np.logspace(-1, 1, 3).tolist(),  # had problems with [10]
    'learning_rate': [0.1, 0.3, ],
    'max_depth': [4],
    'scale_pos_weight': [10000],
    'n_estimators': [70, ],  # 200 is ok if using early stopping.
    # 'nthread': [8],
    'silent': [1],
    'subsample': [0.8, ],
}

_SKLEARN_ENSEMBLE_GRID_BIG = {
    'n_estimators': [10, 30, 60, 100],
    'criterion': ['gini', 'entropy'],
    'max_depth': [4, 5, ],
    # 'min_samples_leaf': [0.0001, ],
    'max_leaf_nodes': [150, ],
    'n_jobs': [-1],
    'oob_score': [True],
    'bootstrap': [True],
    'class_weight': ['balanced_subsample', ],
}

_ISOLATIONFOREST_GRID_BIG = {
    'n_estimators': [500, ],
    'contamination': [1e-4],
    'n_jobs': [-1],
    'bootstrap': [True],
}

_LOGISTIC_GRID = {
    'penalty': ['l1', 'l2', ],
    'C': np.logspace(-3, 3, 5),
    'tol': [1e-5],
    'class_weight': ['balanced', ],
    'solver': ['saga', ],
    'max_iter': [10000, ],
    'n_jobs': [-1],
}

_DT_GRID = {
    'max_depth': [4, 7, 10],
    'class_weight': ['balanced', ],
}

_MLPCLASSIFIER_GRID_BIG = {
    'activation': ['logistic', 'relu', ],
    'alpha': np.logspace(-4, 1, 4),
    # 'batch_size': 'auto',
    'beta_1': [0.9, ],
    'beta_2': [0.999, ],
    'early_stopping': [True],
    # 'epsilon': [1e-08, 1e-5],
    'hidden_layer_sizes': [
        # (128, ),
        (1024, ),
        (2048, ),
        3 * (500, ),
    ],
    # 'learning_rate': ['constant', 'adaptive'],
    'learning_rate': ['adaptive', ],
    # 'learning_rate_init': 0.001,
    # 'max_iter': 200,
    # 'momentum': 0.9,
    # 'nesterovs_momentum': True,
    # 'power_t': 0.5,
    # 'random_state': None,
    'shuffle': [True, ],
    # 'solver': 'adam',
    # 'tol': 0.0001,
    # 'validation_fraction': 0.1,
    # 'verbose': False,
    # 'warm_start': False
}

_GNB_GRID_BIG = {'priors': [None, ]}

# Expose all grids with this single object.
GRIDS = {
    'randomforestclassifier': _SKLEARN_ENSEMBLE_GRID_BIG,
    'extratreesclassifier': _SKLEARN_ENSEMBLE_GRID_BIG,
    'isolationforest': _ISOLATIONFOREST_GRID_BIG,
    'xgbclassifier': _XGBOOST_GRID,
    'gaussiannb': _GNB_GRID_BIG,
    'logisticregression': _LOGISTIC_GRID,
    'decisiontreeclassifier': _DT_GRID,
    'mlpclassifier': _MLPCLASSIFIER_GRID_BIG,
}
