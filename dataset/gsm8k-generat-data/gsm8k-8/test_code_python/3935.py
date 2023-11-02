def solution():
    # Define the initial number of each type of pet
    dogs = 30
    cats = 28
    lizards = 20

    # Calculate the number of pets adopted
    dogs_adopted = 0.5 * dogs
    cats_adopted = 0.25 * cats
    lizards_adopted = 0.2 * lizards

    # Calculate the remaining number of each type of pet
    dogs_remaining = dogs - dogs_adopted
    cats_remaining = cats - cats_adopted
    lizards_remaining = lizards - lizards_adopted

    # Calculate the total number of pets after adoptions and new arrivals
    total_pets = dogs_remaining + cats_remaining + lizards_remaining + 13
    result = total_pets
    return result

print(solution())