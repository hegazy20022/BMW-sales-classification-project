BMW SALES CLASSIFICATION PROJECT

this project focuses on classifying bmw car sales into two categories: high and low
the classification is based on features like region, price, color, and most importantly, sales volume

dataset overview

the dataset contains 50,000 rows and 11 columns
the target column is sales_classification with two classes:

low representing 70% of the data

high representing 30%

there’s a slight imbalance between the classes but it’s still manageable

step 1 - initial exploration

no missing values or outliers were found
some columns were categorical and needed preprocessing
i checked for any logical order in the categorical features but since there was none, i used one-hot encoding
a groupby analysis was done to calculate feature averages by class
then i plotted a heatmap which showed that sales_volume had the strongest correlation with the target compared to all other features

step 2 - data preprocessing

i defined the features (x) and the target (y)
then i split the data into training and testing sets using stratify to keep the class distribution balanced
transformations were fitted only on the training set and then applied to the test set to prevent data leakage
label encoding was used for the target variable
i used columntransformer to handle both scaling and encoding and wrapped everything inside a pipeline for cleaner implementation

step 3 - modeling and evaluation

i tested several classification algorithms without tuning to get baseline results
svm, naive bayes, and logistic regression gave the best performance
other models either overfit or showed weak results

svm

since the dataset was large and svm is computationally heavy i used a sample of the data for hyperparameter tuning
best parameters were gamma 0.1 and c 10 with rbf kernel since most relationships were nonlinear
i also used class_weight=balanced to handle class imbalance

test results were:

accuracy: 0.9891

precision: 0.9893

recall: 0.9891

f1 score: 0.9891

confusion matrix showed:

true negatives (high): 3024

false positives (high): 34

false negatives (low): 10

true positives (low): 6941

this means the model had very few errors and performed slightly better on the low class

naive bayes

naive bayes gave slightly higher accuracy than svm
it was also a bit better at predicting the high class based on the confusion matrix
the roc curve for the low class showed a clear upward trend away from the random baseline which confirmed the model’s strength

artificial neural network

i built an ann with three hidden layers and one output layer using sigmoid activation
applied l2 regularization and dropout to reduce overfitting
used adam optimizer and added early stopping to stop training at the best point

both the roc curve and confusion matrix showed excellent results for both classes

step 4 - interpreting the results

naive bayes is fast and efficient which makes it a great choice for large datasets like this
if the number of features increases and the relationships become more complex then ann would be the better option
to confirm stability i ran stratified 5-fold cross-validation
performance was consistent across all folds with almost no variation
this confirmed that the models generalize well and are not overfitting

feature importance

i used permutation importance to find which features had the most impact
it confirmed what the heatmap showed earlier
sales_volume was by far the most important feature
keeping this feature in future datasets is critical to maintain strong performance

final thoughts

all three models gave excellent results
naive bayes is ideal when you need speed and scalability
svm also performs well but is more computationally expensive
ann will be the best option if the data becomes more complex in the future
most importantly sales_volume should always be included in future versions of the dataset to keep performance high
