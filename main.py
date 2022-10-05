import lights_system
import data_classes


if __name__ == '__main__':
    ls = lights_system.LightsSystem()

    ls.execute_instruction(
        data_classes.Instruction(
            'on',
            data_classes.Coordinate(0, 0),
            data_classes.Coordinate(9, 9)
        )
    )
    ls.execute_instruction(
        data_classes.Instruction(
            'off',
            data_classes.Coordinate(1, 2),
            data_classes.Coordinate(5, 4)
        )
    )
    r = ls.calculate_on_lights()
    a=2
