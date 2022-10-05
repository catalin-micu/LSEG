import input_processors
import lights_system


if __name__ == '__main__':
    ls = lights_system.LightsSystem()
    ins_list = []
    for i in input_processors.read_instructions('coding_challenge_input.txt'):
        ins_list.append(input_processors.create_instruction_object(i))

    ls.execute_multiple_instructions(ins_list)
    print('Part one:', f'{ls.calculate_on_lights()} lights are on', sep='\n')

    uls = lights_system.UpgradedLightsSystem()
    uls.execute_multiple_instructions(ins_list)
    print(
        'Part two:', f'Sum of on lights is {uls.calculate_on_lights()} taking into account brightness levels', sep='\n'
    )
    a=2
