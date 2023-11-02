def solution():
    red_lights = 12
    blue_lights = 3 * red_lights
    green_lights = 6
    total_colored_lights = red_lights + blue_lights + green_lights + 5
    total_lights = 2 * total_colored_lights
    white_lights = total_lights - (red_lights + blue_lights + green_lights + 5)
    result = white_lights
    return result

print(solution())