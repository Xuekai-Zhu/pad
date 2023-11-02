def solution():
    """A dog runs through a field and is joined by a group of 4 cats. 2 rabbits join each cat and 3 hares join each rabbit. How many animals are running through the field?"""
    # Calculate the number of animals in each group
    cats = 4
    rabbits = cats * 2
    hares = rabbits * 3

    # Calculate the total number of animals running through the field
    total_animals = 1 + cats + rabbits + hares  # add 1 for the dog

    # Display the total number of animals
    result = total_animals
    return result

print(solution())