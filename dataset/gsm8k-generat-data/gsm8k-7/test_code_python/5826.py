def solution():
    num_dogs = 1
    num_cats = 4
    num_rabbits_per_cat = 2
    num_hares_per_rabbit = 3

    # Calculate the total number of rabbits
    total_rabbits = num_cats * num_rabbits_per_cat

    # Calculate the total number of hares
    total_hares = total_rabbits * num_hares_per_rabbit

    # Calculate the total number of animals
    total_animals = num_dogs + num_cats + total_rabbits + total_hares
    result = total_animals
    return result

print(solution())