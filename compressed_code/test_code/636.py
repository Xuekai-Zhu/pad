def solution():
    
    total_pets = 189
    dog_ratio = 10/27
    cat_ratio = 17/27
    total_dogs = dog_ratio * total_pets
    remaining_dogs = total_dogs - 10
    result = remaining_dogs
    return result

print(solution())