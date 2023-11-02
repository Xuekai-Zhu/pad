def solution():
    """The Reptile House at the zoo has 5 fewer animals than 3 times the number of animals housed in the Rain Forest exhibit. If the Reptile House has 16 animals, how many are in the Rain Forest exhibit?"""
    reptile_animals = 16
    rainforest_animals = (reptile_animals + 5) / 3
    result = rainforest_animals
    return result

print(solution())