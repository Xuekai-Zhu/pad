def solution():
    """A dog runs through a field and is joined by a group of 4 cats. 2 rabbits join each cat and 3 hares join each rabbit. How many animals are running through the field?"""
    dog = 1
    cats = 4
    rabbits = 2 * cats
    hares = 3 * rabbits
    total_animals = dog + cats + rabbits + hares
    result = total_animals
    return result

print(solution())