def solution():
    
    total_slices = 16
    initial_slices_eaten = total_slices / 4
    remaining_slices = total_slices - initial_slices_eaten
    yves_slices = remaining_slices / 4
    remaining_slices -= yves_slices
    siblings_slices = 2 * 2
    remaining_slices -= siblings_slices
    result = remaining_slices
    return result

print(solution())