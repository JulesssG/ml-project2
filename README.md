# Earthquake Detection from Seismological Data
This project is part of the Machine Learning course, CS-433, at EPFL. In this project we use data from the ObsPy library to train a model that try to predict the presence of earthquake in a given period of time. We'll do a lot of feature engineering to try to extract enough information for this prediction based on the time serie of the amplitude measured by seismological sensors. All our choices and approaches are explained in the _report.pdf_ file in the _report_ folder.

## Setup of the code
All the code of the data processing and model creation is present in a single jupyter notebook: *eq_detection.ipynb*, that way it is simpler to see the approach and steps taken directly with the code. To be able to run the notebook, the user need the following libraries: obspy, numpy, panda, re, math and matplotlib. The architecture needed regarding the data (loading of the raw data of the pre-processed data) is explained in the descriptions of the functions. The user can run the model without any prior work, preparation of the environment is only needed if one want to have the raw data, not only the features.

## Structure of the repository
This repository is quite simple it contains:
- This README file
- The notebook *eq_detection.ipynb* containing the code
- A folder _helpers_ containing helpers functions and scripts
- A folder _processed-data_ containing the preprocessed data so that one can run the model without effort. This contains the features (X), the truth values (y) and the metadata (the period of time it corresponds to) for the supervised machine learning model.
- A folder _data_ containing the catalogs, the truth values raw as downloaded using the ObsPy library
