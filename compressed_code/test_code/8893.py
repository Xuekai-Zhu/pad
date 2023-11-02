def solution():
    
    initial_dogs = 30
    initial_cats = 28
    initial_lizards = 20
    new_pets = 13
    adopted_dogs = initial_dogs * 0.5
    adopted_cats = initial_cats * 0.25
    adopted_lizards = initial_lizards * 0.2
    remaining_dogs = initial_dogs - adopted_dogs
    remaining_cats = initial_cats - adopted_cats
    remaining_lizards = initial_lizards - adopted_lizards
    total_pets = remaining_dogs + remaining_cats + remaining_lizards + new_pets
    result = total_pets
    return result

print(solution())