def solution():
    red_lights = 12
    blue_lights = 3 * red_lights
    green_lights = 6
    total_lights = red_lights + blue_lights + green_lights
    num_lights_left = 5
    num_lights_bought = total_lights - num_lights_left
    num_white_lights = num_lights_bought - (red_lights + blue_lights + green_lights)
    result = num_white_lights
    return result

print(solution())