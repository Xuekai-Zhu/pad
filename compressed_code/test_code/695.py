def solution():
    
    wash_cycle_time = 0.75    
    dry_cycle_time = 1        
    total_loads = 8
    total_wash_time = wash_cycle_time * total_loads
    total_dry_time = dry_cycle_time * total_loads
    total_time = total_wash_time + total_dry_time
    result = total_time
    return result

print(solution())