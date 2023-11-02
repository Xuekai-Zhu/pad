def solution():
    """Frankie's parents let him have many pets. He has six more snakes than he has cats. He has one less parrot than cats. Six of his pets have four legs. He has 2 dogs. How many pets does he have in total?"""
    # Define the number of dogs
    dogs = 2

    # Define the number of pets with 4 legs
    four_legs = 6

    # Calculate the number of cats
    cats = four_legs - dogs - 2

    # Calculate the number of snakes
    snakes = cats + 6

    # Calculate the number of parrots
    parrots = cats - 1

    # Calculate the total number of pets
    total_pets = dogs + cats + snakes + parrots

    # return the result
    result = total_pets
    return result

print(solution())