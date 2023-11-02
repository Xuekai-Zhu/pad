def solution():
    
    red_lights = 12
    blue_lights = red_lights * 3
    green_lights = 6
    total_colored_lights = red_lights + blue_lights + green_lights
    remaining_colored_lights = 5
    initial_white_lights = total_colored_lights + remaining_colored_lights
    result = initial_white_lights
    return result

print(solution())