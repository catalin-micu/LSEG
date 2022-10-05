import input_processors
import lights_system
import data_classes


if __name__ == '__main__':
    ls = lights_system.LightsSystem()
    l = []
    for i in input_processors.read_instructions('dev_input.txt'):
        l.append(input_processors.create_instruction_object(i))

    ls.execute_multiple_instructions(l)
    # ls.execute_instruction(l[0])
    # ls.execute_instruction(l[1])
    res = ls.calculate_on_lights()
    a=2
