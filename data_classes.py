from dataclasses import dataclass


@dataclass
class Coordinate:
    row: int
    column: int


@dataclass
class Instruction:
    command: str
    start: Coordinate
    stop: Coordinate

