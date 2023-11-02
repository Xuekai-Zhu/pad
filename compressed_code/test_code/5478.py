def solution():
    
    total_slices = 12
    leftover_slices = total_slices / 2
    remaining_slices = leftover_slices - (leftover_slices / 3)
    result = remaining_slices
    return result

print(solution())