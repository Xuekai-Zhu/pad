def solution():
    # Calculate the number of time-outs for throwing food
    throwing_timeouts = 5 * 4 - 1
    
    # Calculate the number of time-outs for swearing
    swearing_timeouts = int(throwing_timeouts / 3)
    
    # Calculate the total number of time-outs
    total_timeouts = 5 + throwing_timeouts + swearing_timeouts
    
    # Calculate the total time spent in time-out
    total_time = total_timeouts * 5
    result = total_time
    return result

print(solution())