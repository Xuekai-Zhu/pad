def solution():
    """Emily goes fishing and has a very busy day. She catches 4 trout, 3 catfish, and 5 bluegills. If the trout weigh 2 pounds each, the catfish weigh 1.5 pounds each, and the bluegills weigh 2.5 pounds each, how many total pounds of fish did she catch?"""
    # Define the weight in pounds of each type of fish
    TROUT_WEIGHT = 2
    CATFISH_WEIGHT = 1.5
    BLUEGILL_WEIGHT = 2.5

    # Define the number of each type of fish caught
    trout_catch = 4
    catfish_catch = 3
    bluegill_catch = 5

    # Calculate the total weight of the trout
    trout_weight = trout_catch * TROUT_WEIGHT

    # Calculate the total weight of the catfish
    catfish_weight = catfish_catch * CATFISH_WEIGHT

    # Calculate the total weight of the bluegills
    bluegill_weight = bluegill_catch * BLUEGILL_WEIGHT

    # Calculate the total weight of all the fish caught
    total_weight = trout_weight + catfish_weight + bluegill_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())