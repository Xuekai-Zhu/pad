def solution():
    """Gina is participating in a neighborhood clean-up filling bags with litter. She was able to collect two bags of litter herself. The rest of the neighborhood together collected 82 times as much as Gina did by herself. Each bag of litter weighs 4 pounds. How many pounds was all the litter they collected?"""
    # Define the weight of one bag of litter
    BAG_WEIGHT = 4

    # Calculate the weight of the litter collected by Gina
    gina_weight = 2 * BAG_WEIGHT

    # Calculate the weight of the litter collected by the rest of the neighborhood
    neighborhood_weight = 82 * gina_weight

    # Calculate the total weight of the litter collected
    total_weight = gina_weight + neighborhood_weight

    result = total_weight
    return result

print(solution())