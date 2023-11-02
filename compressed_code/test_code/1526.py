def solution():
    
    total_slices = 16
    eaten_slices = int(total_slices * 0.75)
    leftover_slices = total_slices - eaten_slices
    result = leftover_slices
    return result

print(solution())