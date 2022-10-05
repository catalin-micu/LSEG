import pytest

import data_classes
import lights_system


def test_lights_system_constructor(monkeypatch):
    monkeypatch.setattr('const.GRID_DIMENSION', 10)
    ls = lights_system.LightsSystem()
    assert len(ls.grid) == 10, 'Something went wrong when mocking the constant'
    assert len(ls.grid[0]) == 10, 'Something went wrong when mocking the constant'


@pytest.mark.parametrize('command', ['on', 'off', 'toggle'])
def test_execute_instruction(monkeypatch, mocker, command):
    monkeypatch.setattr('const.GRID_DIMENSION', 10)
    ls = lights_system.LightsSystem()
    mocked_method = mocker.patch('lights_system.LightsSystem._execute')
    ls.execute_instruction(
        data_classes.Instruction(command, data_classes.Coordinate(0, 0), data_classes.Coordinate(1, 1))
    )
    mocked_method.assert_called_once()


def test_calculate_on_lights(monkeypatch):
    monkeypatch.setattr('const.GRID_DIMENSION', 10)
    ls = lights_system.LightsSystem()
    ls.grid[0][0] = 230
    ls.grid[0][5] = True
    ls.grid[9][9] = 'abc'
    actual = ls.calculate_on_lights()

    assert actual == 3


@pytest.mark.parametrize(
    'start, stop, value, toggle, on_lights',
    [
        (data_classes.Coordinate(0, 0), data_classes.Coordinate(9, 9), True, False, 100)
    ]
)
def test__execute(monkeypatch, start, stop, value, toggle, on_lights):
    monkeypatch.setattr('const.GRID_DIMENSION', 10)
    ls = lights_system.LightsSystem()
    ls._execute(start, stop, value, toggle)

    actual = 0
    for row in ls.grid:
        actual += sum(row)

    assert actual == on_lights
