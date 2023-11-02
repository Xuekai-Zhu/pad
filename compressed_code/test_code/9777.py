def solution():
    
    
    max_people_no_dog = 6
    
    
    max_people_with_dog = int(max_people_no_dog * 2/3)
    
    
    person_weight = 140
    dog_weight = person_weight * 1/4
    
    
    total_weight = max_people_with_dog * person_weight + dog_weight
    
    return total_weight

print(solution())