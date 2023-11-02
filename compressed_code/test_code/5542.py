def solution():
    
    route1_time = 6 + (2 * 6) + (1/3 * (6 + (2 * 6)))
    route2_time = 14 + (2 * 14)
    time_diff = route2_time - route1_time
    result = time_diff
    return result

print(solution())