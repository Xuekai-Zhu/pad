def solution():
    num_dogs = 4
    num_parrots = 8
    nails_per_dog = 4 * 4  # 4 nails on each of 4 feet
    nails_per_parrot = 3 * 2 + 4  # 3 claws on each of 2 legs + 1 extra toe

    # Calculate the total number of nails
    total_nails = num_dogs * nails_per_dog + num_parrots * nails_per_parrot
    result = total_nails
    return result

print(solution())