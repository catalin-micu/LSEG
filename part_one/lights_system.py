from part_one import const


class LightsSystem:
    def __init__(self):
        self.grid = []
        for i in range(const.GRID_DIMENSION):
            self.grid.append([0] * const.GRID_DIMENSION)

    def execute_instruction(self, instruction: str):
        pass

    def calculate_on_lights(self) -> int:
        pass
