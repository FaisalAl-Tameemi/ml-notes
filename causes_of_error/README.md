## Causes of Error

Now that we have covered some basic metrics for measuring model performance, let us turn our attention to reasons why models exhibit errors in the first place.

In model prediction there are two main sources of errors that a model can suffer from. Bias due to a model being unable to represent the complexity of the underlying data and variance due to a model being overly sensitive to the limited data it has been trained on. We will go over both in a bit more detail.


## Error due to Bias - Accuracy and Underfitting

Bias occurs when a model has enough data but is not complex enough to capture the underlying relationships. As a result, the model consistently and systematically misrepresents the data, leading to low accuracy in prediction. This is known as underfitting.

Simply put, bias occurs when we have an inadequate model. An example might be when we have objects that are classified by color and shape, for example easter eggs, but our model can only partition and classify objects by color. It would therefore consistently mislabel future objects--for example labeling rainbows as easter eggs because they are colorful.

Another example would be continuous data that is polynomial in nature, with a model that can only represent linear relationships. In this case it does not matter how much data we feed the model because it cannot represent the underlying relationship. To overcome error from bias, we need a more complex model.

## Error due to Variance - Precision and Overfitting

When training a model, we typically use a limited number of samples from a larger population. If we repeatedly train a model with randomly selected subsets of data, we would expect its predictons to be different based on the specific examples given to it. Here variance is a measure of how much the predictions vary for any given test sample.

Some variance is normal, but too much variance indicates that the model is unable to generalize its predictions to the larger population. High sensitivity to the training set is also known as overfitting, and generally occurs when either the model is too complex or when we do not have enough data to support it.

We can typically reduce the variability of a model's predictions and increase precision by training on more data. If more data is unavailable, we can also control variance by limiting our model's complexity.

## Improving the Validity of a Model

There is a trade-off in the value of simplicity or complexity of a model given a fixed set of data. If it is too simple, our model cannot learn about the data and misrepresents the data. However if our model is too complex, we need more data to learn the underlying relationship. Otherwise it is very common for a model to infer relationships that might not actually exist in the data.

The key is to find the sweet spot that minimizes bias and variance by finding the right level of model complexity. Of course with more data any model can improve, and different models may be optimal.

To learn more about bias and variance, we recommend [this essay by Scott Fortmann-Roe.](http://scott.fortmann-roe.com/docs/BiasVariance.html)

In addition to the subset of data chosen for training, what features you use from a given dataset can also greatly affect the bias and variance of your model.
