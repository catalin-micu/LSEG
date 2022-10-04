import lights_system


if __name__ == '__main__':
    ls = lights_system.LightsSystem()
    ls.grid[0][0] = 1
    ls.grid[0][5] = 1
    ls.grid[9][9] = 1
    r = ls.calculate_on_lights()
    a=2
