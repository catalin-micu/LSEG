from dataclasses import dataclass


@dataclass
class Coordinate:
    row: int
    column: int

    def __repr__(self):
        return f'({self.row}, {self.column})'


@dataclass
class Instruction:
    command: str
    start: Coordinate
    stop: Coordinate

    def __repr__(self):
        return f'{self.command} for subgrid between {self.start} and {self.stop}'

