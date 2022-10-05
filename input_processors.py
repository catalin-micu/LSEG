import pathlib
from typing import Generator, Union

import data_classes


def read_instructions(path_to_file: Union[str, pathlib.Path]) -> Generator:
    """
    Yields each row in the input file, since the input file instructions are separated by new lines
    :param path_to_file: input file to parse
    :return: generator with each instruction
    """
    with open(path_to_file, 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()


def create_instruction_object(str_ins: str) -> data_classes.Instruction:
    """
    Breaks the instruction string down and creates equivalent dataclass object for further use
    :param str_ins: instruction in string form
    :return: instruction as dataclass object
    """
    str_ins = str_ins.replace('turn', '').strip()
    command = str_ins.split()[0]
    str_ins = str_ins.replace(command, '')
    start_coordinates, stop_coordinates = str_ins.split('through')
    start_row, start_column = start_coordinates.split(',')
    stop_row, stop_column = stop_coordinates.split(',')

    start = data_classes.Coordinate(int(start_row), int(start_column))
    stop = data_classes.Coordinate(int(stop_row), int(stop_column))
    validate_start_and_stop(start, stop)

    return data_classes.Instruction(command=command, start=start, stop=stop)


def validate_start_and_stop(start: data_classes.Coordinate, stop: data_classes.Coordinate):
    if stop.row < start.row:
        raise ValueError('Stop row cannot be smaller than start row')
    if stop.row == start.row and stop.column < start.column:
        raise ValueError('When start and stop are on the same row, stop column cannot be smaller than start column')
