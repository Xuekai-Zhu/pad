def solution():
    num_packs = 12
    pack_weight = 250
    leftover_sugar = 20

    # Calculate the total weight of sugar in all packs, including leftovers
    total_weight = (num_packs * pack_weight) + leftover_sugar

    # Calculate the weight of sugar before it was divided into packs
    starting_weight = total_weight - leftover_sugar
    result = starting_weight
    return result

print(solution())