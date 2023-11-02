def solution():
    
    initial_cells = 1
    doubling_time = 20
    growth_periods = 4 * 60 // doubling_time  
    final_cells = initial_cells * 2 ** growth_periods
    result = final_cells
    return result

print(solution())