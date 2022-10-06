from typing import Optional, List, Any

import numpy as np

import const
import data_classes
import custom_logger


module_logger = custom_logger.create_logger(__name__)


class LightsSystem:
    def __init__(self, default_value: Any = False, value_type: Any = bool):
        """
        For part 1
        Lights system controller that handles the instructions. The grid is a list of numpy arrays in order to cover the
        edge case of somebody manually changing a value of one item to 500 and then calling calculate_on_lights. I am
        using numpy arrays strictly to restrict the types of the items inside. This make calculate_on_lights method much
        easier to implement.
        """
        self.logger = module_logger
        self.grid = []
        for i in range(const.GRID_DIMENSION):
            self.grid.append(np.array([default_value] * const.GRID_DIMENSION, dtype=value_type))
        self.logger.debug(f'Initialized {self.__class__.__name__} with {const.GRID_DIMENSION} grid dimensions')

    def execute_multiple_instructions(self, instructions: List[data_classes.Instruction]):
        for ins in instructions:
            self.execute_instruction(ins)

    def execute_instruction(self, instruction: data_classes.Instruction):
        """
        Execute instruction based on command
        :param instruction: dataclass that fully defines the instruction
        """
        # I am not satisfied with this if/else, there is duplicate code, but I don't see anything better rn
        self.logger.debug(f'Executing instruction "{instruction}"')
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
            self.logger.warning(f'Encountered useless instruction; stop coordinate is (0, 0). Skipping...')
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
        self.logger.debug('Calculating grid status...')
        nb_on_lights = 0
        for row in self.grid:
            nb_on_lights += sum(row)

        return nb_on_lights


class UpgradedLightsSystem(LightsSystem):
    def __init__(self):
        super().__init__(default_value=0, value_type=int)

    def execute_instruction(self, instruction: data_classes.Instruction):
        """
        Execute instruction based on command
        :param instruction: dataclass that fully defines the instruction
        """
        self.logger.debug(f'Executing instruction "{instruction}"')
        if instruction.command == 'on':
            self._execute(instruction.start, instruction.stop, value=1)
        elif instruction.command == 'off':
            self._execute(instruction.start, instruction.stop, value=-1)
        else:
            self._execute(instruction.start, instruction.stop, value=2)

    def _execute(self, start: data_classes.Coordinate, stop: data_classes.Coordinate, value: int = None, **kwargs):
        """
        Generic method that can execute any type of instruction
        :param **kwargs: placeholder for toggle
        :param start: first affected light
        :param stop: last affected light
        :param value: value to add for each light
        """
        if stop.row == 0 and stop.column == 0:
            self.logger.warning(f'Encountered useless instruction; stop coordinate is (0, 0). Skipping...')
            return
        if stop.row == start.row:
            for i in range(start.column, stop.column + 1):
                new_value = self.grid[start.row][i] + value
                self.grid[start.row][i] = new_value if new_value >= 0 else 0
            return

        for i in range(start.row, stop.row + 1):
            for j in range(start.column, stop.column + 1):
                new_value = self.grid[i][j] + value
                self.grid[i][j] = new_value if new_value >= 0 else 0
