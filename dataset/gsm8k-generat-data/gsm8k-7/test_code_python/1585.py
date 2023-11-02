def solution():
    num_dogs = 3
    num_cats = 2
    num_ferrets = 1

    # Each animal needs 4 shoes
    num_shoes_needed = (num_dogs + num_cats + num_ferrets) * 4

    result = num_shoes_needed
    return result

print(solution())