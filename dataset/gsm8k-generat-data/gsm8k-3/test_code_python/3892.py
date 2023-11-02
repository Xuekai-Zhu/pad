def solution():
    """Gina is participating in a neighborhood clean-up filling bags with litter. She was able to collect two bags of litter herself. The rest of the neighborhood together collected 82 times as much as Gina did by herself. Each bag of litter weighs 4 pounds. How many pounds was all the litter they collected?"""
    # Define the number of bags of litter Gina collected
    gina_bags = 2

    # Calculate the total number of bags collected by the neighborhood
    neighborhood_bags = gina_bags * 82

    # Calculate the total weight of all the litter collected
    total_weight = (gina_bags + neighborhood_bags) * 4

    # Display the total weight
    result = total_weight
    return result

print(solution())