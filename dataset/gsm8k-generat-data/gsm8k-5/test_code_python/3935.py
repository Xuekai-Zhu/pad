def solution():
    dogs = 30
    cats = 28
    lizards = 20
    new_pets = 13

    # Calculate the number of pets adopted
    adopted_dogs = dogs * 0.5
    adopted_cats = cats * 0.25
    adopted_lizards = lizards * 0.2

    # Calculate the number of pets remaining
    remaining_dogs = dogs - adopted_dogs
    remaining_cats = cats - adopted_cats
    remaining_lizards = lizards - adopted_lizards

    # Add the new pets to the remaining pets
    total_dogs = remaining_dogs + (new_pets * 0.5)
    total_cats = remaining_cats + (new_pets * 0.25)
    total_lizards = remaining_lizards + (new_pets * 0.2)

    # Calculate the total number of pets
    total_pets = total_dogs + total_cats + total_lizards
    result = total_pets
    return result

print(solution())