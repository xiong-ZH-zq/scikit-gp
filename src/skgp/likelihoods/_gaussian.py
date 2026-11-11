from numbers import Real

import numpy as np

from skgp.likelihoods import BaseLikelihood


class GaussianLikelihood(BaseLikelihood):
    def __init__(self, noise_variance=1e-10):

        if (
            (not isinstance(noise_variance, Real))
            or (noise_variance < 0)
            or (not np.isfinite(noise_variance))
        ):
            raise ValueError("noise_variance should be a finite positive real value.")

        self.noise_variance = noise_variance

    def log_prob(self, y, f):

        y = np.asarray(y)
        f = np.asarray(f)
        variance = self.noise_variance

        return -0.5 * (np.log(2.0 * np.pi * variance) + (y - f) ** 2 / variance)
