def solution():
    """Gina is participating in a neighborhood clean-up filling bags with litter. She was able to collect two bags of litter herself. The rest of the neighborhood together collected 82 times as much as Gina did by herself. Each bag of litter weighs 4 pounds. How many pounds was all the litter they collected?"""
    gina_bags = 2
    neighborhood_bags = 82 * gina_bags
    total_bags = gina_bags + neighborhood_bags
    total_weight = total_bags * 4
    result = total_weight
    return result

print(solution())