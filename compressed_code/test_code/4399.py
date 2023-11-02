def solution():
    
    num_slices = 12
    breakfast_slices = num_slices / 3
    lunch_slices = 2
    remaining_slices = num_slices - breakfast_slices - lunch_slices
    result = remaining_slices
    return result

print(solution())