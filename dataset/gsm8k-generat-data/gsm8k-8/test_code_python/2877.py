def solution():
    # Calculate the time it takes for each route
    time_route1 = 1500 / 75
    time_route2 = 750 / 25

    # Find the faster route by comparing the times
    if time_route1 < time_route2:
        faster_route_time = time_route1
    else:
        faster_route_time = time_route2

    result = faster_route_time
    return result

print(solution())