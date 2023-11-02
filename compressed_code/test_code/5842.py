def solution():
    
    total_weight_lost = 103
    first_person_weight_lost = 27
    second_person_weight_lost = first_person_weight_lost - 7
    last_two_people_weight_lost = (total_weight_lost - first_person_weight_lost - second_person_weight_lost) / 2
    result = last_two_people_weight_lost
    return result

print(solution())