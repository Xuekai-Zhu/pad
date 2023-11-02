def solution():
    
    running_timeouts = 5
    food_timeouts = 5 * running_timeouts - 1
    swearing_timeouts = food_timeouts / 3
    total_timeouts = running_timeouts + food_timeouts + swearing_timeouts
    total_time = total_timeouts * 5
    result = total_time
    return result

print(solution())