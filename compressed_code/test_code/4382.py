def solution():
    
    total_slices = 12
    john_slices = 3
    sam_slices = 2 * john_slices
    remaining_slices = total_slices - john_slices - sam_slices
    result = remaining_slices
    return result

print(solution())