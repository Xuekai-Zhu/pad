def solution():
    """Emily goes fishing and has a very busy day. She catches 4 trout, 3 catfish, and 5 bluegills. If the trout weigh 2 pounds each, the catfish weigh 1.5 pounds each, and the bluegills weigh 2.5 pounds each, how many total pounds of fish did she catch?"""
    # Define the weight of each type of fish and the number caught
    TROUT_WEIGHT = 2
    CATFISH_WEIGHT = 1.5
    BLUEGILL_WEIGHT = 2.5
    num_trout = 4
    num_catfish = 3
    num_bluegill = 5

    # Calculate the total weight of each type of fish caught
    total_trout_weight = num_trout * TROUT_WEIGHT
    total_catfish_weight = num_catfish * CATFISH_WEIGHT
    total_bluegill_weight = num_bluegill * BLUEGILL_WEIGHT

    # Calculate the total weight of all fish caught
    total_weight = total_trout_weight + total_catfish_weight + total_bluegill_weight

    # return the result
    result = total_weight
    return result

print(solution())