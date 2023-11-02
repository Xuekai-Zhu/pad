def solution():
    # Calculate the number of animals in each group
    cats = 4
    rabbits = cats * 2
    hares = rabbits * 3

    # Calculate the total number of animals
    total_animals = 1 + cats + rabbits + hares
    result = total_animals
    return result

print(solution())