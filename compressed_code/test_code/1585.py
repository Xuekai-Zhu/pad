def solution():
    
    total_slices = 8 + 14
    eaten_slices = 9 + 9
    remaining_slices = total_slices - eaten_slices
    slices_per_person = remaining_slices / 2
    result = slices_per_person
    return result

print(solution())