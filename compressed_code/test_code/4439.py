def solution():
    
    total_time = 120  
    cycle_time = 10 + 5  
    num_cycles = total_time // cycle_time  
    remaining_time = total_time % cycle_time  
    num_partial_cycles = 1 if remaining_time >= 10 else 0  
    result = num_cycles + num_partial_cycles
    return result

print(solution())