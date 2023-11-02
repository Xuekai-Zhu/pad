def solution():
    
    time_to_prepare = 1 + (15/60) + 2 + (30/60) + (15/60)    
    opening_time = 6    
    latest_time = opening_time - time_to_prepare
    result = latest_time
    return result

print(solution())