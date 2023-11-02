def solution():
    # Calculate the time taken on the first route
    time_first_route = 1500 / 75  # Distance / speed

    # Calculate the time taken on the second route
    time_second_route = 750 / 25  # Distance / speed

    # Find the fastest route by comparing the times
    if time_first_route < time_second_route:
        fastest_time = time_first_route
    else:
        fastest_time = time_second_route

    result = fastest_time
    return result

print(solution())