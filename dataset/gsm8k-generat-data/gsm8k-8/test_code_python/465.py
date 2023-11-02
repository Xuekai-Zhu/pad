def solution():
    # Define the time for the first route with all green lights
    route1_time = 10

    # Define the time added for each red light
    red_light_time = 3

    # Calculate the maximum added time for all 3 red lights
    max_red_light_time = red_light_time * 3

    # Calculate the total time for the first route with all red lights
    route1_max_time = route1_time + max_red_light_time

    # Calculate the difference in time between the two routes
    route_difference = route1_max_time - 14

    result = route_difference
    return result

print(solution())