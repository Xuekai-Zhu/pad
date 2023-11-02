def solution():
    
    total_slices = 8
    joe_darcy_slices = total_slices * (1/2)
    carl_slices = total_slices * (1/4)
    remaining_slices = total_slices - joe_darcy_slices - carl_slices
    result = remaining_slices
    return result

print(solution())