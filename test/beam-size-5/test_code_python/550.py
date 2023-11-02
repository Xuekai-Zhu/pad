def solution():
    
    cold_time = 16
    warm_time = 2 + 2 * cold_time
    hot_distance = 3
    hot_time = hot_distance * hot_time
    time_difference = hot_time - cold_time
    result = time_difference
    return result

print(solution())