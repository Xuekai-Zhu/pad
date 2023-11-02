def solution():
    num_dogs = 2
    num_legs_per_pet = 4

    # Calculate the total number of legs of the pets with 4 legs
    num_legs_of_4_legs_pets = num_legs_per_pet * 6

    # Calculate the total number of cats
    num_cats = num_legs_of_4_legs_pets // (num_legs_per_pet * 2) - 1

    # Calculate the total number of snakes
    num_snakes = num_cats + 6

    # Calculate the total number of parrots
    num_parrots = num_cats - 1

    # Calculate the total number of pets that Frankie has
    total_num_pets = num_dogs + num_cats + num_snakes + num_parrots
    result = total_num_pets
    return result

print(solution())