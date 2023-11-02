def solution():
    num_dogs = 30
    num_cats = 28
    num_lizards = 20
    
    adopted_dogs = num_dogs * 0.5
    adopted_cats = num_cats * 0.25
    adopted_lizards = num_lizards * 0.2
    
    remaining_dogs = num_dogs - adopted_dogs
    remaining_cats = num_cats - adopted_cats
    remaining_lizards = num_lizards - adopted_lizards
    
    total_pets = remaining_dogs + remaining_cats + remaining_lizards + 13
    
    result = total_pets
    return result

print(solution())