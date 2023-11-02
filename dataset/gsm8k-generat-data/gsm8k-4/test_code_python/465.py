def solution():
    """A man is returning home from work and trying to decide which route to take. His first route option includes 3 stoplights. This route will take him 10 minutes if all three lights are green, but each light that is red will add 3 minutes to the trip. The second route does not include any stoplights and takes 14 minutes. If the man chooses the first route, how much longer will his trip be if all 3 stoplights are red?"""
    # Define the time it takes to travel each route with all green lights
    time_green_lights = 10

    # Define the time it takes to travel the second route
    time_second_route = 14

    # Define the time that is added for each red light
    time_per_red_light = 3

    # Calculate the maximum possible time for the first route
    time_max = time_green_lights + (3 * time_per_red_light)

    # Calculate the difference between the maximum possible time and the time with all green lights
    time_diff = time_max - time_green_lights

    # Return the difference
    result = time_diff
    return result

print(solution())