def solution():
    """In a neighborhood, the number of rabbits pets is twelve less than the combined number of pet dogs and cats. If there are two cats for every dog, and the number of dogs is 60, how many pets in total are in the neighborhood?"""
    dogs = 60
    cats = dogs * 2
    rabbits = (dogs + cats) - 12
    total_pets = dogs + cats + rabbits
    result = total_pets
    return result

print(solution())