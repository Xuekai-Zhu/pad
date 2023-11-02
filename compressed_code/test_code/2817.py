def solution():
    
    bottle_size = 2000 
    sip_size = 40 
    time_per_sip = 5 
    total_sips = bottle_size / sip_size
    total_time_in_minutes = total_sips * time_per_sip
    result = total_time_in_minutes
    return result

print(solution())