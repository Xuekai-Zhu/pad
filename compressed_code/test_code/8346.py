def solution():
    
    initial_roses = 40
    stolen_roses = 4
    remaining_roses = initial_roses - stolen_roses
    num_people = 9
    roses_per_person = remaining_roses / num_people
    result = roses_per_person
    return result

print(solution())