def solution():
    num_red_lights = 12
    num_blue_lights = 3 * num_red_lights
    num_green_lights = 6
    num_colored_lights = num_red_lights + num_blue_lights + num_green_lights + 5

    # Calculate the total number of lights that Malcolm bought
    total_lights = num_colored_lights + num_white_lights

    # Calculate the initial number of white lights
    num_white_lights = total_lights - num_colored_lights

    result = num_white_lights
    return result

print(solution())