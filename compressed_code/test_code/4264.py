def solution():
    
    total_time = 1 + (15/60) + 2 + (30/60) + (15/60) 
    open_time = 6
    latest_arrival_time = open_time - total_time
    result = latest_arrival_time
    return result

print(solution())