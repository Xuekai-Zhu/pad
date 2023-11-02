def solution():
    
    total_slices = 3 * 12
    total_cost = 72
    cost_per_slice = total_cost / total_slices
    cost_of_5_slices = cost_per_slice * 5
    result = cost_of_5_slices
    return result

print(solution())