def solution():
    route1_distance = 1500
    route1_speed = 75

    route2_distance = 750
    route2_speed = 25

    # Calculate the time it takes for each route
    route1_time = route1_distance / route1_speed
    route2_time = route2_distance / route2_speed

    # Determine which route is faster
    if route1_time < route2_time:
        fastest_route_time = route1_time
    else:
        fastest_route_time = route2_time

    result = fastest_route_time
    return result

print(solution())