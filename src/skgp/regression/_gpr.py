"""
Gaussian process regression.
"""

from sklearn.base import (
    BaseEstimator,
    # MultiOutputMixin,
    RegressorMixin,
)

from skgp.likelihoods import GaussianLikelihood


class GaussianProcessRegressor(RegressorMixin, BaseEstimator):
    """Gaussian process regressor (GPR) compatible with scikit-learn `GaussianProcessRegressor`

    Parameters
    ----------
    kernel : kernel instance, default=None
        The kernel specifying the covariance function of the GP.
        If `None` is passed,
        the kernel `ConstantKernel() * RBF()` is used as default.

    likelihood : likelihood instance, default = None
        The likelihood specifying the likelihood function of the GP.
        If `None` is passed, the likelihood `GaussianLikelihood` is used as default.
    """

    def __init__(self, kernel=None, *, likelihood=None):
        self.kernel = kernel
        self.likelihood = likelihood
