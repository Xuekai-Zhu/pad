def solution():
    # Calculate the total time it takes to go and come back using route A
    total_time_route_a = 2 * 5

    # Calculate the total time it takes to go and come back using route B
    total_time_route_b = 2 * 2

    # Calculate the time saved by taking route B
    time_saved = total_time_route_a - total_time_route_b
    result = time_saved
    return result

print(solution())