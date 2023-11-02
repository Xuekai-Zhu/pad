def solution():
    """A pet store has six dogs for sale. They have half as many cats, twice as many birds, and thrice as many fish for sale. How many animals are for sale in the pet store?"""
    dogs = 6
    cats = dogs / 2
    birds = dogs * 2
    fish = dogs * 3
    total_animals = dogs + cats + birds + fish
    result = total_animals
    return result

print(solution())