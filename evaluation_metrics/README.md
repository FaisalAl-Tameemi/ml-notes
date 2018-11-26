
## Before Picking a Metric

In building machine learning models we need to pick a performance metric to test how well our model is performing. We will cover several metrics, and which one we use will depend on the problem we are trying to solve.

Before we can pick a performance metric, it is important to recognize that machine learning is about learning from data to make predictions. For this class and the follow up course "Supervised Machine Learning" we will focus on labeled data. The predictions we will be making will be classification and regression.

When testing your model, it is important to partition your dataset into training and testing data. If the training and test datasets are not kept seperate, we can experience a problem called data leakage. That is, our model will be making predictions on data it has already seen. Then its performance may not be representative of what will happen with novel data! What we need is an independent set of data to verify that the model can generalize well to data outside the training examples. We will go over common sources of model errors in the next lesson and cover how to properly split your datasets in the Data Modeling & Validation section of this course.

## Classification and Regression

Classification is about deciding which categories new instances belong to. For example we can organize objects based on whether they are square or round, or we might have data about different passengers on the Titanic like in project 0, and want to know whether or not each passenger survived. Then when we see new objects we can use their features to guess which class they belong to.

In regression, we want to make a prediction on continuous data. For example we might have a list of different people's height, age, and gender and wish to predict their weight. Or perhaps, like in the final project of this course, we have some housing data and wish to make a prediction about the value of a single home.

The problem at hand will determine how we choose to evaluate a model.

## Classification vs Regression Metrics

In classification we want to see how often a model correctly or incorrectly identifies a new example, whereas in regression we might be more interested to see how far off the model's prediction is from the real true value.

For the rest of this lesson we will discuss various performance metrics. For classification we will cover accuracy, precision, recall, and F-score. For regression we will go over mean absolute error and mean squared error.

## Classification Metrics

For classification we are dealing with models that make discrete predictions.

That is to say these models decide which of a given set of categories a certain data point belongs to. Using a set of data kept for testing, we can measure on this testing set which points were accurately classified, and which were not.

## Accuracy

The most basic and common classification metric is accuracy. Accuracy here is described as the proportion of items classified or labeled correctly.

For instance if a classroom has 14 boys and 16 girls, can a facial recognition software correctly identify all boys and all girls? If the software can identify 10 boys and 8 girls, then the software is 60% accurate.

accuracy = number of correctly identified instances / all instances

Accuracy is the default metric used in the `.score()` method for classifiers in sklearn.

Problem with Accuracy: http://cl.ly/3o0c3N040z3w

## Precision and Recall

http://cl.ly/3Z3f1C0h2p2P

http://cl.ly/3s140w3u2I1H

http://cl.ly/1r0T1f2t2s2x

http://cl.ly/3i3e3o3g161U

## F1 Score

Now that you've seen precision and recall, another metric you might consider using is the F1 score. F1 score combines precision and recall relative to a specific positive class.

The F1 score can be interpreted as a weighted average of the precision and recall, where an F1 score reaches its best value at 1 and worst at 0:

`F1 = 2 * (precision * recall) / (precision + recall)`

For more information about F1 score how to use it in sklearn, check out the documentation [here](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score).

## Regression Metrics

As mentioned earlier for regression problems we are dealing with model that makes continuous predictions. In this case we care about how close the prediction is.

For example with height & weight predictions it is unreasonable to expect a model to 100% accurately predict someone's weight down to a fraction of a pound! But we do care how consistently the model can make a close prediction--perhaps with 3-4 pounds.

## Mean Absolute Error

One way to measure error is by using absolute error to find the predicted distance from the true value. **The mean absolute error takes the total absolute error of each example and averages the error based on the number of data points.** By adding up all the absolute values of errors of a model we can avoid canceling out errors from being too high or below the true values and get an overall error metric to evaluate the model on.

For more information about mean absolute error and how to use it in sklearn, check out the documentation [here](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error).

## Mean Squared Error

Mean squared is the most common metric to measure model performance. In contrast with absolute error, the residual error (the difference between predicted and the true value) is squared.

Some benefits of squaring the residual error is that error terms are positive, it emphasizes larger errors over smaller errors, and is differentiable. Being differentiable allows us to use calculus to find minimum or maximum values, often resulting in being more computationally efficient.

For more information about mean squared error and how to use it in sklearn, check out the documentation [here](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error).

## Regression Scoring Functions

In addition to error metrics, Scikit-learn contains two scoring metrics which scale generally from 0 to 1, with values of 0 being bad and 1 being perfect performance.

These are the metrics that you'll use in the project at the end of the course. They have the advantage of looking similar to classification metrics, with numbers closer to 1.0 being good scores and bad scores tending to be near 0.

One of these is the [R2 score](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score), which computes the coefficient of determination of predictions for true values. This is the default scoring method for regression learners in scikit-learn.

The other is the [explained variance score](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score).

While we will not treat these metrics in detail just now, one important point to remember is that the default metrics for regression are "higher is better"; that is, higher scores indicate better performance. When using the error metrics described previously, we will need to overwrite this preference.
