def solution():
    """A dog runs through a field and is joined by a group of 4 cats. 2 rabbits join each cat and 3 hares join each rabbit. How many animals are running through the field?"""
    # Define the initial number of animals
    dog = 1
    cats = 4
    rabbits = cats * 2
    hares = rabbits * 3

    # Calculate the total number of animals
    total_animals = dog + cats + rabbits + hares

    # return the result
    result = total_animals
    return result

print(solution())