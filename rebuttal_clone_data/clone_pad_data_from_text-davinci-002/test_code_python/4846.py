def solution():
    doubling_time = 20
    initial_cells = 1
    time_grown = 4 * 60
    doubling_time_in_minutes = doubling_time * 60
    number_of_doublings = time_grown / doubling_time_in_minutes
    total_cells = initial_cells * 2 ** number_of_doublings
    result = total_cells
    
    return result

print(solution())