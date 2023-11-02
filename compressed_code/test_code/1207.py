def solution():
    
    remaining_slices = 4
    slices_per_person = 2
    slices_eaten = 16 - remaining_slices
    num_people = slices_eaten / slices_per_person
    result = num_people
    return result

print(solution())