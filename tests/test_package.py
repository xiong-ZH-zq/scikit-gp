from importlib.metadata import version

import skgp

# check is package import is valid
def test_package_import():
    assert skgp is not None
    assert version("scikit-gp")