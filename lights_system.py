import numpy as np
from array import array

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
        if instruction.command == 'turn on':
            self.turn_on(instruction.start, instruction.stop)
        elif instruction.command == 'turn off':
            self.turn_off(instruction.start, instruction.stop)
        else:
            self.toggle(instruction.start, instruction.stop)

    def turn_on(self, start: data_classes.Coordinate, stop: data_classes.Coordinate):
        pass

    def turn_off(self, start: data_classes.Coordinate, stop: data_classes.Coordinate):
        pass

    def toggle(self, start: data_classes.Coordinate, stop: data_classes.Coordinate):
        pass

    def calculate_on_lights(self) -> int:
        """
        Calculate how many lights are on in total; a light is on if on its grid coordinate the value is True
        :return:
        """
        nb_on_lights = 0
        for row in self.grid:
            nb_on_lights += sum(row)

        return nb_on_lights
