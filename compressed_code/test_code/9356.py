def solution():
    
    total_dogs = 12
    back_legs_per_dog = 2
    all_legs_per_dog = 4
    total_back_legs = (total_dogs / 2) * back_legs_per_dog
    total_paws_on_ground = total_back_legs + ((total_dogs / 2) * all_legs_per_dog)
    result = total_paws_on_ground
    return result

print(solution())