# DSND Capstone Project

This project has two parts, which are intended to be run in different environments.  Each is described in its own README file.

## Jupyter Notebook

The file `dog_app.ipynb`, provided by Udacity.  Setup pertaining to running the notebook is described in `README_train.md`.  This is the original README provided with the notebook.  Because the notebook requires a lot of computational power, it is strongly recommended to run the notebook in the Udacity provided workspace with GPU enabled.

This notebook has been worked through and lots of comments have been added.  Project Definition, Analysis and Conclusion sections were added to the notebook.  Various other rubric requirements are addressed in inline prose throughout the document.

Running the notebook produces (among other things) the file `weights.best.Inception.hdf5`, which is a required input file for the web application.  A version of this file from a prior execution of the the notebook has already been checked into the repository, so it's not necessary to run the notebook in order to run the web app.

## Web Application

The web application uses prebuilt models for making predictions.  This is a lightweight operation and is intended to be run on your local PC.  The setup and operation of the web app is documented in `README_web.md`.