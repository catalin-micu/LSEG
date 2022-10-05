import pathlib

import pytest

import data_classes
import input_processors


def test_read_instructions():
    generator_items = list(
        input_processors.read_instructions(pathlib.Path(__file__).parent / 'files' / 'instructions.txt')
    )
    assert len(generator_items) == 5
    assert 'testing\n' in generator_items


def test_validate_start_and_stop():
    input_processors.validate_start_and_stop(
        start=data_classes.Coordinate(268, 631), stop=data_classes.Coordinate(735, 814)
    )


@pytest.mark.parametrize(
    'start, stop', [
        (data_classes.Coordinate(10, 10), data_classes.Coordinate(9, 12)),
        (data_classes.Coordinate(10, 10), data_classes.Coordinate(10, 9))
    ]
)
def test_validate_start_and_stop_raises(start, stop):
    with pytest.raises(ValueError):
        input_processors.validate_start_and_stop(start, stop)


@pytest.mark.parametrize(
    'str_ins, obj_ins', [
        (
                'turn on 268,631 through 735,814',
                data_classes.Instruction('on', data_classes.Coordinate(268, 631), data_classes.Coordinate(735, 814))
        ),
        (
            'toggle 549,969 through 612,991',
            data_classes.Instruction('toggle', data_classes.Coordinate(549, 969), data_classes.Coordinate(612, 991))
        )
    ]
)
def test_create_instruction_object(str_ins, obj_ins):
    actual = input_processors.create_instruction_object(str_ins)
    assert actual == obj_ins
