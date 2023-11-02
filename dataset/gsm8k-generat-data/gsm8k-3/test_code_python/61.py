def solution():
    """A bear is preparing to hibernate for the winter and needs to gain 1000 pounds. At the end of summer, the bear feasts on berries and small woodland animals. During autumn, it devours acorns and salmon. It gained a fifth of the weight it needed from berries during summer, and during autumn, it gained twice that amount from acorns. Salmon made up half of the remaining weight it had needed to gain. How many pounds did it gain eating small animals?"""
    # Define the target weight the bear needs to gain
    target_weight = 1000

    # Calculate the weight gained from berries in the summer
    summer_weight = target_weight / 5

    # Calculate the weight gained from acorns in the autumn
    autumn_weight = summer_weight * 2

    # Calculate the remaining weight needed to gain
    remaining_weight = target_weight - summer_weight - autumn_weight

    # Calculate the weight gained from salmon
    salmon_weight = remaining_weight / 2

    # Calculate the weight gained from small animals
    small_animals_weight = remaining_weight - salmon_weight

    # Return the weight gained from small animals
    result = small_animals_weight
    return result

print(solution())