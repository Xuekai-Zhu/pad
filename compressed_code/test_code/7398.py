def solution():
    
    small_pizza_slices = 8
    large_pizza_slices = 14
    total_slices = small_pizza_slices + large_pizza_slices
    eaten_slices = 9 + 9
    remaining_slices = total_slices - eaten_slices
    slices_per_person = remaining_slices / 2
    result = slices_per_person
    return result

print(solution())