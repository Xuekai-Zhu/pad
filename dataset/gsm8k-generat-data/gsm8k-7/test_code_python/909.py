def solution():
    num_frogs = 160
    num_dogs = num_frogs / 2
    num_cats = num_dogs * 0.8

    # Calculate the total number of animals in the compound
    total_animals = num_frogs + num_dogs + num_cats
    result = total_animals
    return result

print(solution())