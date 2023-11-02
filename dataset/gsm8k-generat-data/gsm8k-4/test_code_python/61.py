def solution():
    """A bear is preparing to hibernate for the winter and needs to gain 1000 pounds. At the end of summer, the bear feasts on berries and small woodland animals. During autumn, it devours acorns and salmon. It gained a fifth of the weight it needed from berries during summer, and during autumn, it gained twice that amount from acorns. Salmon made up half of the remaining weight it had needed to gain. How many pounds did it gain eating small animals?"""
    # Define the total weight the bear needs to gain and initialize the weight gained from berries and acorns
    total_weight_gain = 1000
    berry_weight_gain = total_weight_gain / 5
    acorn_weight_gain = berry_weight_gain * 2

    # Calculate the remaining weight the bear needs to gain and the weight gained from salmon
    remaining_weight_gain = total_weight_gain - berry_weight_gain - acorn_weight_gain
    salmon_weight_gain = remaining_weight_gain / 2

    # Calculate the weight gained from small animals
    small_animal_weight_gain = total_weight_gain - berry_weight_gain - acorn_weight_gain - salmon_weight_gain

    # Return the result
    result = small_animal_weight_gain
    return result

print(solution())