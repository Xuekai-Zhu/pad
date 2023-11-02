def solution():
    total_roses = 40
    stolen_roses = 4
    remaining_roses = total_roses - stolen_roses
    people_to_give_roses = 9
    roses_per_person = remaining_roses / people_to_give_roses
    result = roses_per_person
    return result

print(solution())