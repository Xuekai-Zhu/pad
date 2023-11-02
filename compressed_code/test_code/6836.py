def solution():
    
    lawns_per_hour = 2
    lawns_per_day = 8
    days = 2
    total_lawns = lawns_per_day * days
    time_per_lawn = 30 / 60 
    total_time = total_lawns * time_per_lawn
    result = total_time
    return result

print(solution())