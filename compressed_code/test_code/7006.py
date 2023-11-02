def solution():
    
    running_time_outs = 5
    food_time_outs = (5 * running_time_outs) - 1
    swearing_time_outs = food_time_outs / 3
    total_time_outs = running_time_outs + food_time_outs + swearing_time_outs
    time_in_minutes = total_time_outs * 5
    result = time_in_minutes
    return result

print(solution())