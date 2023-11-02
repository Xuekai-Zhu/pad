def solution():
    
    total_slices = 2 * 8
    jerry_slices = (3/8) * total_slices
    remaining_slices = total_slices - jerry_slices
    tom_slices = remaining_slices / 2
    result = tom_slices
    return result

print(solution())