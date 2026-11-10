# scikit-gp
A Python Package implementing Gaussian Process algorithms that are compatible with [scikit-learn](https://scikit-learn.org/stable/index.html). 

This package aims to implement classic Gaussian process models like Gaussian process regressors and classifiers.

## Why yet another GP package?

- [GPytorch](https://gpytorch.ai/) is great for GP modeling, but may be too large for scenarios without deep learning.
- Some GP models in scikit-learn uses old methods, e.g. [`GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html) is based on Laplace approximation algorithm.

Therefore, scikit-gp is trying to realize GP models based on several papers.


