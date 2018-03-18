"""Run all the desired analysis of your project.

Those analysis should be defined elsewhere.

"""

import data_utilities as du

import constants  # noqa
import data_exploration
import data_loading
import data_processing
import grid_search
import models

# pylama: ignore=D103


def main():
    """Execute all the analyzes."""
    # Set the random seed for the entire project.
    du.set_random_seed(0)
    # Rationale: ensure reproducibility of the results.

    # Functions with side effects here are best method to perform the task.
    # Each function should cleanly load and import whathever is necessary in
    # their own methods.
    #
    # This prevents memory from building up in this stage.

    # Load and prepare the data.
    data_loading.main()
    # Rationale: Load and prepare the data to be used in other parts of your
    # code.

    # Perform exploratory data analyses.
    data_processing.main()
    # Load and prepare the data to be used in other parts of your code.

    # Perform exploratory data analyses.
    data_exploration.main()
    # Rationale: conduct exploratory data analyses.

    # Perform grid search.
    grid_search.main()
    # Rationale: perform grid search as part of machine learning best
    # practices.

    # Evaluate the model results.
    models.main()
    # Rationale: this is the reporting part: metrics, predicts, etc.


if __name__ == '__main__':
    main()
