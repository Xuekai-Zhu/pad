def solution():
    time_route_a = 5  # It takes 5 hours to arrive at Boston via route A
    time_route_b = 2  # It takes 2 hours to arrive at Boston via route B

    # Total time taken if Joseph takes route A to Boston and back
    total_time_a = time_route_a * 2

    # Total time taken if Joseph takes route B to Boston and back
    total_time_b = (time_route_b * 2) + time_route_b

    # Difference in time taken between route A and route B
    time_saved = total_time_a - total_time_b
    result = time_saved
    return result

print(solution())