from __future__ import division, absolute_import, print_function

import sys
if sys.version[:2] == (3, 7):
    import pickle5 as pickle
else:
    import pickle

from numpy.testing import assert_raises, assert_, assert_equal

if sys.version_info[:2] >= (3, 4):
    from importlib import reload
else:
    from imp import reload

def test_numpy_reloading():
    # gh-7844. Also check that relevant globals retain their identity.
    import numpy as np
    import numpy._globals

    _NoValue = np._NoValue
    VisibleDeprecationWarning = np.VisibleDeprecationWarning
    ModuleDeprecationWarning = np.ModuleDeprecationWarning

    reload(np)
    assert_(_NoValue is np._NoValue)
    assert_(ModuleDeprecationWarning is np.ModuleDeprecationWarning)
    assert_(VisibleDeprecationWarning is np.VisibleDeprecationWarning)

    assert_raises(RuntimeError, reload, numpy._globals)
    reload(np)
    assert_(_NoValue is np._NoValue)
    assert_(ModuleDeprecationWarning is np.ModuleDeprecationWarning)
    assert_(VisibleDeprecationWarning is np.VisibleDeprecationWarning)

def test_novalue():
    import numpy as np
    assert_equal(repr(np._NoValue), '<no value>')
    assert_(pickle.loads(pickle.dumps(np._NoValue)) is np._NoValue)
