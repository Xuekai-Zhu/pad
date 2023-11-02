def solution():
    # Define the weight of each type of fish
    trout_weight = 2
    catfish_weight = 1.5
    bluegill_weight = 2.5

    # Calculate the total weight of each type of fish
    total_trout_weight = 4 * trout_weight
    total_catfish_weight = 3 * catfish_weight
    total_bluegill_weight = 5 * bluegill_weight

    # Calculate the total weight of all the fish
    total_weight = total_trout_weight + total_catfish_weight + total_bluegill_weight
    result = total_weight
    return result

print(solution())