def solution():
    
    old_time_per_mile = 10
    new_time_per_mile = 13
    distance = 5
    time_difference_per_mile = new_time_per_mile - old_time_per_mile
    extra_time = time_difference_per_mile * distance
    result = extra_time
    return result

print(solution())