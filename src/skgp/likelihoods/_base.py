from abc import ABC, abstractmethod

from sklearn.base import BaseEstimator


class BaseLikelihood(BaseEstimator, ABC):
    """Base class for likelihood functions."""

    @abstractmethod
    def log_prob(self, y, f):
        """Return the elementwise log probability of observations given f."""
        raise NotImplementedError
