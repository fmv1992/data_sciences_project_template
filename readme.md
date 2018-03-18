# Data sciences project organization

This project outlines a good approach for managing data sciences projects.

You can check a working example at: my [data_sciences_project_example](https://github.com/fmv1992/data_sciences_project_example).  
**Note**: The project above does not reflect the most recent version of this project.

## Motivation

Organization is crucial for every data sciences project.

Have you ever started with a minimal 'two file project' and the ended up with a big mess of files? Disorganization can hurt your project's effectiveness.

This structure is a 'convergent evolution' of different projects of mine related to data sciences. It is the result of several trial-and-error iterations with different project layouts with their different requirements. And it is by no means definitive.

Recently I've been trying to use [GNU make](https://en.wikipedia.org/wiki/Make_(software)) to ease organization and reproducibility of a data sciences project. So far it has proven to be effective.

## Project structure

1. `code`: this is where all of your could should be. Code is code, data is
   data. Never mix them.
1. `data`: Data is sacred. Put them all here and make it your shrine.
1. `output`: Put all of your results here. This folder is 'flushable' so every
   result has to be reproducible.
1. `tmp`: Save intermediate results here (more on that below).

### Code files

Lets start by outlining what goes where:

* `code/python/constants.py`:
    * Assign project-wide variables and functions.
        * Examples: paths, number of CPUs to use (in the case of parallel processing), etc.
    * It should be the first file imported by other files. Ideally it should not import other files within the same project.
    * Must contain assertions for most of its assignments (when applicable; such as paths).
        * This saves time when long-running functions try to output to non existent paths.
* `code/python/data_exploration.py`:
    * Provide data exploration functions.
    * Should be isolated from other functions and have its `main` function called by the `main` function in the `main.py` file.
* `code/python/data_loading.py`:
    * Provide data loading and preparation functions.
    * Provide adequate data splitting methods (e.g. out of time versus out of sample).
    * Must ensure data is properly passed to other functions of the module, including data type management (e.g. categorical versus boolean).
    * Do not mix data processing with data loading (see below).
* `code/python/data_processing.py`:
    * Provide data processing functions.
    * Among its actions are feature extraction and feature transformations.
    * Should combine data transformations into functions. Those functions should be called from the `main` function in the `main.py` file and output new dataframes (hdf format is a good idea), including the simplest dataframe.
        * This workflow ensures uniformity in data management and facilitates the workflow of data.
    * Do not mix data processing with data loading (see above).
* `code/python/grid_search.py`:
    * Provide grid search functions.
    * Should combine models x datasets (data transformations) x grid search.
    * Should expose best results that are easily combined with models. In the
      end the data scientist wants the best combination of: model + data
      + hyperparameter/grid.
* `code/python/grids.py`:
    * Should be a file containing the grids to be investigated during the hyper parameter tuning phase.
* `code/python/main.py`:
    * Run all the desired analysis of your project. Just hit play (i.e. `make run`) and go grab a coffee.
    * Must execute all pertinent functions and generate all desired results. One command and your project is executed.
    * Contain imports and high level function calls only. No legwork is done here.
    * Call main functions defined in other files. Also calls specific functions from other files.
    * May have other module-level simple functions' definitions (such as filtering warnings).
    * All complexity should be kept away from it and encapsulated in the respective python file.
* `code/python/models.py`:
    * Provide model loading functions.
    * Execute models' results analyses.

See [data_sciences_project_example](https://github.com/fmv1992/data_sciences_project_example) for an illustration of those concepts.
**Note**: The project above does not reflect the most recent version of this project.

### Benefits of such layout

1. Project level organization: You know what goes where. Very sharp separation of code, temporary files, data and output.
1. Python module level organization: simple file names that obviates where to put your new ideas.
1. Flat structure: leads to simple importing in python and easier module understanding.
1. Good modularity/complexity trade-off: Having a total of around seven files helps when you need search or find a place to put your functions.

* `code/python/main.py`:
    * By moving away all the complexity and syntax boilerplate to other functions, your project becomes easily 'pluggable'. Commenting/Uncommenting single lines makes it easy to skip functions during the development phase:

        ~~~~~~
        # Costly data processing function.
        data_exploration.main(dataframe)  # very easily commented out
        ~~~~~~

## General workflow

I consider all of my projects to be a combination of the following pipeline:

~~~~~~
                                                Algorithm selection
                                                |  |  |  |  |  |  |
                                                v  v  v  v  v  v  v

                                        ->      +-----------------+
                                        ->      |                 |
 Data loading -> Data transformation    ->      |   grid search   |
                 (algorithm dependent)  ->      |                 |
                                        ->      +-----------------+

                                                |  |  |  |  |  |  |
                                                v  v  v  v  v  v  v

                                                +-----------------+
                                                |                 |
                                                |    Reporting    |
                                                |                 |
                                                +-----------------+

~~~~~~

Which equates to:

~~~~~~
Datasets x Algorithms x Hyperparameters
~~~~~~

Sometimes there is even a third combination like different output variables.

This is the most flexible scenario. It may be simplified by using just one dataset. The order of the looping matters in this case: often data loading is slower so it should be in outermost loop.

## Tips from best practices (and a lot of mistakes)

1. **One dataset, one model**: One data set means one model in the end. Don't try to keep two different models/datasets on the same structure. Move your functions to an independent module and split them.
1. **Serializie costly computations but know when to flush them**: Do create a temporary files so that costly computations are rarely recomputed. However be sure to cleanly clean your results to ensure reproducibility.
1. Split your train and test dataframes into separate file. Minimize the risk of combining them.

## TODO

1. See the module configparse of python!
    * Promising for: grid searching specification.
        * Data is data, remember?
    * Feature combination: different arrays/datasets can be combined differently.

1. Apply to my ongoing data sciences competition.

1. Data exploration pre and post processing shall have their own functions. This is not clearly defined in the current workflow.

1. Consider using a makefile for improved automation.

1. Specify data analyses/exploration just after data set loading and just after dataset processing. That is, split what currently is one thing in two things.

1. Consider moving models results to a reporting file `reporting.py`.
