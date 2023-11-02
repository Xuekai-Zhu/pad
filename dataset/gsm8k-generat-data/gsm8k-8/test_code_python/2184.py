def solution():
    # Define the variables
    snakes = cats + 6
    parrots = cats - 1
    four_legged_pets = 6
    dogs = 2

    # Calculate the number of cats
    cats = four_legged_pets - snakes - parrots - dogs

    # Calculate the total number of pets
    total_pets = snakes + cats + parrots + dogs
    result = total_pets
    return result

print(solution())