def solution():
    # Calculate the total number of nails on the dogs
    nails_on_dogs = 4 * 4 * 4  # 4 dogs, 4 nails per foot, 4 feet per dog

    # Calculate the total number of claws on the parrots
    claws_on_parrots = 8 * (3 * 2 + 4)  # 8 parrots, 3 claws per leg (except 1 with 4), 2 legs per parrot

    # Calculate the total number of nails Cassie needs to cut
    total_nails = nails_on_dogs + claws_on_parrots
    result = total_nails
    return result

print(solution())