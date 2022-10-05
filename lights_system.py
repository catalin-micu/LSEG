from typing import Optional, List

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

    def execute_multiple_instructions(self, instructions: List[data_classes.Instruction]):
        for ins in instructions:
            self.execute_instruction(ins)

    def execute_instruction(self, instruction: data_classes.Instruction):
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
        """
        if stop.row == 0 and stop.column == 0:
            return
        if stop.row == start.row:
            for i in range(start.column, stop.column + 1):
                self.grid[start.row][i] = value if not toggle else not self.grid[start.row][i]
            return

        for i in range(start.row, stop.row + 1):
            for j in range(start.column, stop.column + 1):
                self.grid[i][j] = value if not toggle else not self.grid[i][j]

    def calculate_on_lights(self) -> int:
        """
        Calculate how many lights are on in total; a light is on if on its grid coordinate the value is True
        """
        nb_on_lights = 0
        for row in self.grid:
            nb_on_lights += sum(row)

        return nb_on_lights
