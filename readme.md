# Data sciences project organization

This package outlines a good approach for managing data sciences projects.

You can check a working example at: my
[data_sciences_project_example](https://github.com/fmv1992/data_sciences_project_example).


## Motivation

Organization is crucial for every data sciences project.

Have you ever started with a minimal 'two file project' and the ended up with
a big mess of files?

Disorganization can hurt your project's effectiveness.

This structure is a 'convergent evolution' of different projects of mine
related to data sciences. It is the result of several trial-and-error
iterations with different project layouts with their different requirements.

Project structure:

1. `code`: this is where all of your could should be. Code is code, data is
   data.
1. `data`: Data is sacred. Put them all here and make it your shrine.
1. `output`: Put all of your results here. This folder is 'flushable' so every
   result has to be reproducible.
1. `tmp`: Save intermediate results here (more on that below).


## Code files

Lets start by outlining what goes where:
* `code/python/constants.py`: 
    * Assign project-wide variables and functions.
        * Examples: paths, number of CPUs to use (in the case of parallel
          processing), etc.
    * It should be the first file imported by other files.
    * Must contain assertions for all of its assignments (when applicable; such
      as paths).
        * This saves time when long-running functions try to output to non
          existent paths.
* `code/python/data_exploration.py`: 
    * Provide data exploration functions.
    * Should be isolated from other functions and have its `main` function
      called by the `main` function in the `main.py` file.
* `code/python/data_loading.py`: 
    * Provide data loading and preparation functions.
    * Provide adequate data splitting methods (out of time versus out of
      sample).
    * Must ensure data is properly passed to other functions of the module,
      including data type management (e.g. categorical versus boolean).
    * Do not mix data processing with data loading (see below).
* `code/python/data_processing.py`: 
    * Provide data processing functions.
    * Among its actions are feature extraction and feature transformations.
    * Should combine data transformations into functions. Those functions
      should be called from the `main` function in the `main.py` file and
      output new dataframes (in hdf format), including the simplest dataframe.
        * This workflow ensures uniformity in data management and facilitates
          the workflow of data.
    * Do not mix data processing with data loading (see above).
* `code/python/grid_search.py`: 
    * Provide grid search functions.
    * Should combine models x datasets (data transformations) x grid search.
    * Should expose best results per model (that is a data set and a best grid)
      in a function.
* `code/python/main.py`: 
    * Run all the desired analysis of your project.
    * Contains imports and high level function calls only.
    * Calls main functions defined in other files. Also calls specific
      functions from other files.
    * May have other module level simple functions' definitions (such as
      filtering warnings).
    * All complexity should be kept away from it and encapsulated in the
      respective py file.
* `code/python/models.py`: 
    * Provide model loading functions.
    * Execute models' results analyses (to be changed to its own module).


### Benefits of such layout

1. You know what goes where: very sharp separation of code, temporary files,
   data and output.
1. Modules are well defined: simple file names that you where your new idea
   fits.
1. Flat structure: leads to simple importing in python and easier
   understanding.
1. Good modularity/complexity trade-off: Having around seven files helps when
   you need search or find a place to put your functions.

<!--
* `code/python/constants.py`: 
* `code/python/data_exploration.py`: 
* `code/python/data_loading.py`: 
* `code/python/data_processing.py`: 
* `code/python/grid_search.py`: 
-->

* `code/python/main.py`: 
    * By moving away all the complexity and syntax boilerplate to other
      functions, your project becomes easily 'pluggable'.
      Comenting/Uncommenting single lines makes it easy to skip functions
      during the development phase:
        ~~~~~~
        # Costly data processing function.
        data_exploration.main(dataframe)  # very easily commented out
        ~~~~~~

<!--
* `code/python/models.py`: 
-->


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
~~~~~~

Sometimes there is even a third combination like different output variables.

This is the most flexible scenario. It may be simplified by using just one
dataset. The order of the looping matters in this case: often data loading is
slower so it should be in outermost loop.


## Tips from best practices (and a lot of mistakes)

1. One data set means one model in the end. Don't try to keep two different
   models/datasets on the same structure. Move your functions to an independent
   module and split them.
1. Do create a temporary files/results flushing function. Often persistence and
   conditional loading will mix results from different stages of your project.
   This ensures full reproducibility.


## TODO

1. Specify data analyses/exploration just after data set loading and just after
   dataset processing.
1. Move models results to a reporting file.
