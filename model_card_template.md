# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model was created using Scikit Learn's Linear regression model using Cencus Data from 1994 (link here: https://archive.ics.uci.edu/dataset/20/census+income). The features are as follows: 

age,
workclass,
fnlgt,
education,
education-num,
marital-status
,occupation,
relationship,
race,
sex,
capital-gain,
capital-loss,
hours-per-week,
native-country,
salary

This model infers a predicted salary range (less than or greater than $50k) based on the other remaining socio economic factors. 

## Intended Use

This model is intended for educational purposes. More specifically, this model infers a predicted salary range (less than or greater than $50k) based on the other remaining socio economic factors. 

## Training Data
The data used in this model can be found here:  https://archive.ics.uci.edu/dataset/20/census+income. This dataset is from the 1994 Census data. This data does contain missing values.

The 8 categorical features have been one-hot-encoded. The model was trained using the feature of "salary" as the independent variable.

## Evaluation Data
The model was evaluated using test data, isolated using Scikit Learn's train_test_plit() function using the default 80/20 split. 

## Metrics
This model was elvauted on the f_beta, precision and recal scores (all built-in SciKit Learn functions.) For all three scores, the optimal value is 1 and the worst score is 0.

Current Model scores:
Precision: 0.7226 | Recall: 0.2705 | F1: 0.3937

Scores based on slices of the model can be found in the slice_output.txt file. 


## Ethical Considerations

This model uses data that is 30 years out of date and does not likely represent current socio-economic attributes of the present day. 

## Caveats and Recommendations

This model should be used for educational purposes only. To improve this model, updated data and larger sample size should be considered.