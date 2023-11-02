def solution():
    # Calculate the time it takes to complete each trip
    time_route1 = 1500 / 75  # time for first route in hours
    time_route2 = 750 / 25  # time for second route in hours

    # Determine which route is faster and calculate total time
    if time_route1 < time_route2:
        total_time = time_route1
    else:
        total_time = time_route2

    result = total_time
    return result

print(solution())