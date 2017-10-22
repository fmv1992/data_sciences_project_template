# Data sciences project organization

Organization is crucial for every data sciences project.

This package outlines a good approach for managing data sciences projects.

## Motivation

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

## General workflow

## Code files

Lets start by outlining what goes where:

* `code/python/main.py`:
    * Contains imports and high level function calls only.
    * Calls main functions defined in other files.
    * All complexity should be kept away from it and encapsulated in the
      respective py file.
    * Should contain nested for loops to combine different models with possibly
      different pipeline, output variables, etc.
* `code/python/data_loading.py`:
    * Contains data loading and preparation functions.
    * Do not mix data processing with data loading (see below).
    * Must ensure data is properly passed into other functions of the module,
      including data type management (e.g. categorical versus boolean).
* `code/python/constants.py`:
    * Assigns project-wide variables such as paths, number of CPUs to use (in
      the case of parallel processing), etc.
    * It should be the first file imported by other files.
    * Must contain assertions for all of its assignments (when applicable).
* `code/python/data_processing.py`:
    * Contains data processing functions such as feature extraction, feature
      transformations, etc.
    * Do not mix data processing with data loading (see above).
* `code/python/models.py`:
    * Provide model loading and specification.
* `code/python/data_exploration.py`:
    * Provide data exploration functions.
    * Should be isolated from other functions and have its `main` function
      called by the `main` function in the `main.py` file.
                                            * `code/python/grid_search.py`2
    * Provide grid search functions.
    * Grids should be kept in a different module.
    * TODO: keep grids apart in a json or configparse file, etc.

I consider all of my projects to be a combination of the following pipeline:

~~~~~~
                                                Algorithm selection
                                                |  |  |  |  |  |  |
                                                v  v  v  v  v  v  v
                                        ->
 Data loading -> Data transformation    ->
                 (algorithm dependent)  ->
                                        ->
~~~~~~

Sometimes there is even a third combination like different output variables.

So all of these combination should be in the file `code/main.py` in an explicit
loop.


## Tips from best practices (and a lot of mistakes)

1. One data set means one model in the end. Don't try to keep two different
   models/datasets on the same structure. Move your functions to an independent
   model and split them.

## TODO

* `code/python/grid_search.py`: 
    * TODO: keep grids apart in a json or configparse file, etc.
* Where does the dropping of nulls go?
    * Data processing part; feature union
    * ?
