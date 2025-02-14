import numpy as np
import pytest

from pandas import DataFrame


@pytest.fixture
def int_frame_const_col():
    """
    Fixture for DataFrame of ints which are constant per column

    Columns are ['A', 'B', 'C'], with values (per column): [1, 2, 3]
    """
    df = DataFrame(
        np.tile(np.arange(3, dtype="int64"), 6).reshape(6, -1) + 1,
        columns=["A", "B", "C"],
    )
    return df


@pytest.fixture(params=["python", "numba"])
def engine(request):
    if request.param == "numba":
        pytest.importorskip("numba")
    return request.param


@pytest.fixture(params=[0, 1])
def apply_axis(request):
    return request.param
