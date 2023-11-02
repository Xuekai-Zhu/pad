def solution():
    num_trout = 4
    trout_weight = 2
    num_catfish = 3
    catfish_weight = 1.5
    num_bluegills = 5
    bluegill_weight = 2.5

    # Calculate the total weight of all trout that Emily caught
    total_trout_weight = num_trout * trout_weight

    # Calculate the total weight of all catfish that Emily caught
    total_catfish_weight = num_catfish * catfish_weight

    # Calculate the total weight of all bluegills that Emily caught
    total_bluegill_weight = num_bluegills * bluegill_weight

    # Calculate the total weight of all fish that Emily caught
    total_fish_weight = total_trout_weight + total_catfish_weight + total_bluegill_weight
    result = total_fish_weight
    return result

print(solution())