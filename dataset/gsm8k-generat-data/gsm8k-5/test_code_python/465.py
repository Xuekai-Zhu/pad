def solution():
    first_route_green = 10  # Time it takes to travel first route with all green lights
    first_route_red = first_route_green + (3*3)  # Time it takes to travel first route with 3 red lights
    second_route = 14  # Time it takes to travel second route

    # Calculate the difference in time if all 3 lights are red on the first route
    time_difference = first_route_red - first_route_green

    result = time_difference
    return result

print(solution())