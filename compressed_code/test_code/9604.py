def solution():
    
    doubling_time = 20
    growth_period = 4 * 60  
    num_doublings = growth_period / doubling_time
    final_num_cells = 2 ** num_doublings
    result = final_num_cells
    return result

print(solution())