def solution():
    
    total_slices = 16
    leftover_slices = 4
    eaten_slices = total_slices - leftover_slices
    slices_per_person = 2
    num_people = eaten_slices / slices_per_person
    result = num_people
    return result

print(solution())