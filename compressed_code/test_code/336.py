def solution():
    
    green_time = 10
    red_light_time = 3
    num_lights = 3
    all_red_time = green_time + (num_lights * red_light_time)
    second_route_time = 14
    extra_time = all_red_time - second_route_time
    result = extra_time
    return result

print(solution())