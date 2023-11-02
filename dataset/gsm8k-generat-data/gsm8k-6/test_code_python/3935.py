def solution():
    # Calculate the number of adopted pets
    adopted_dogs = 0.5 * 30
    adopted_cats = 0.25 * 28
    adopted_lizards = 0.2 * 20
    total_adopted_pets = adopted_dogs + adopted_cats + adopted_lizards

    # Calculate the number of new pets after one month
    new_pets = 13

    # Calculate the total number of pets after one month
    total_pets = 30 + 28 + 20 - total_adopted_pets + new_pets

    result = total_pets
    return result

print(solution())