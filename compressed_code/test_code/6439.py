def solution():
    
    total_pets = 189
    dog_to_cat_ratio = 10 / 17
    
    
    total_ratio_parts = 10 + 17
    total_dogs = (10 / total_ratio_parts) * total_pets
    
    
    remaining_dogs = total_dogs - 10
    result = remaining_dogs
    
    return result

print(solution())