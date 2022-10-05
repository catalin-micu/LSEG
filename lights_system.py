from typing import Optional

import numpy as np

import const
import data_classes


class LightsSystem:
    # TODO create parent class if time allows? constructor, execute_instruction and calculate_on_lights are common
    #  between par 1 and part 2
    def __init__(self):
        """
        For part 1
        Lights system controller that handles the instructions. The grid is a list of numpy arrays in order to cover the
        edge case of somebody manually changing a value of one item to 500 and then calling calculate_on_lights. I am
        using numpy arrays strictly to restrict the types of the items inside. This make calculate_on_lights method much
        easier to implement.
        """
        self.grid = []
        for i in range(const.GRID_DIMENSION):
            self.grid.append(np.array([False] * const.GRID_DIMENSION, dtype=bool))

    def execute_instruction(self, instruction: data_classes.Instruction):
        # TODO create method which runs a list of instructions
        """
        Execute instruction based on command
        :param instruction: dataclass that fully defines the instruction
        """
        # I am not satisfied with this if/else, there is duplicate code, but I don't see anything better rn
        if instruction.command == 'on':
            self._execute(instruction.start, instruction.stop, value=True)
        elif instruction.command == 'off':
            self._execute(instruction.start, instruction.stop, value=False)
        else:
            self._execute(instruction.start, instruction.stop, toggle=True)

    def _execute(
            self,
            start: data_classes.Coordinate,
            stop: data_classes.Coordinate,
            value: Optional[bool] = None,
            toggle: bool = False
    ):
        """
        Generic method that can execute any type of instruction
        :param start: first affected light
        :param stop: last affected light
        :param value: new value of each light
        :param toggle: whether to toggle or not
        :return:
        """
        for i in range(start.column, const.GRID_DIMENSION):
            self.grid[start.row][i] = value if not toggle else not self.grid[start.row][i]

        for i in range(start.row + 1, stop.row):
            for j in range(const.GRID_DIMENSION):
                self.grid[i][j] = value if not toggle else not self.grid[i][j]

        for i in range(stop.column + 1):
            self.grid[stop.row][i] = value if not toggle else not self.grid[stop.row][i]

    def calculate_on_lights(self) -> int:
        """
        Calculate how many lights are on in total; a light is on if on its grid coordinate the value is True
        :return:
        """
        nb_on_lights = 0
        for row in self.grid:
            nb_on_lights += sum(row)

        return nb_on_lights
