def solution():
    time_route_a = 5
    time_route_b = 2

    # Calculate the total time it takes for Joseph to go to Boston and back using route A
    total_time_a = time_route_a * 2

    # Calculate the total time it takes for Joseph to go to Boston and back using route B
    total_time_b = (time_route_b * 2) + (time_route_a - time_route_b)

    # Calculate how much time Joseph will save by taking route B
    time_saved = total_time_a - total_time_b
    result = time_saved
    return result

print(solution())