import pytest

from part_one import lights_system


def test_lights_system_constructor(monkeypatch):
    monkeypatch.setattr('part_one.const.GRID_DIMENSION', 10)
    ls = lights_system.LightsSystem()
    assert len(ls.grid) == 10, 'Something went wrong when mocking the constant'


def test_execute_instruction():
    ls = lights_system.LightsSystem()
    ls.execute_instruction('bla')


