def solution():
    # Calculate the total number of nails to be trimmed
    nails_per_dog = 4 * 4  # each dog has 4 nails on each foot
    nails_per_parrot = (3 * 2 * 7) + 4  # each parrot has 3 claws on each leg, except for 1 with an extra toe
    total_nails = (nails_per_dog * 4) + (nails_per_parrot * 8)  # Cassie has 4 dogs and 8 parrots
    result = total_nails
    return result

print(solution())