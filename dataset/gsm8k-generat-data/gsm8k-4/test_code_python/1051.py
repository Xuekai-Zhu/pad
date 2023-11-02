def solution():
    """The Reptile House at the zoo has 5 fewer animals than 3 times the number of animals housed in the Rain Forest exhibit. If the Reptile House has 16 animals, how many are in the Rain Forest exhibit?"""
    # Define the number of animals in the Reptile House and the Rain Forest exhibit
    reptile_animals = 16
    rainforest_animals = None

    # Calculate the number of animals in the Rain Forest exhibit using the given equation
    rainforest_animals = (reptile_animals + 5) / 3

    result = int(rainforest_animals)
    return result

print(solution())