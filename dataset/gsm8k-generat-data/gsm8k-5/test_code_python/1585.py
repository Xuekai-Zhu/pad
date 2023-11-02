def solution():
    num_dogs = 3
    num_cats = 2
    num_ferrets = 1

    # Olly needs 4 shoes for each dog and cat
    shoes_per_dog = 4
    shoes_per_cat = 4
    shoes_per_ferret = 2  # Ferrets have 4 paws but need only 2 shoes

    total_shoes = num_dogs * shoes_per_dog + num_cats * shoes_per_cat + num_ferrets * shoes_per_ferret
    result = total_shoes
    return result

print(solution())