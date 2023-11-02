def solution():
    first_route_lights = 3
    first_route_time = 10
    light_delay = 3
    second_route_time = 14
    total_first_route_delay = first_route_lights * light_delay
    total_time_first_route = first_route_time + total_first_route_delay
    total_time_second_route = second_route_time
    time_difference = total_time_first_route - total_time_second_route
    result = abs(time_difference)
    
    return result

print(solution())