import numpy as np
import pytest


@pytest.fixture
def lights_system_grid():
    # this fixture might end up being useless
    grid = []
    for i in range(10):
        grid.append(np.array([False] * 10, dtype=bool))
    return grid
