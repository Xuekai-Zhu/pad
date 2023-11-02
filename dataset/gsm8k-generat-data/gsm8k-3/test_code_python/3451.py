def solution():
    """Lyla, a grocery store owner, bought rice weighing 30 kg less than green beans, which weigh 10 kg more than sugar. While carrying the goods to the store, the bags fell down and 1/3 weight of the rice and 1/5 weight of sugar was lost. If the green beans weighed 60 kgs, then how much did the remaining stock weigh?"""
    # Calculate the weight of sugar
    sugar_weight = 60 - 10 # green beans weigh 10 kg more than sugar
    # Calculate the weight of rice
    rice_weight = sugar_weight - 30 # rice weighs 30 kg less than green beans
    # Calculate the weight of sugar and rice after losing 1/3 and 1/5 of their weight, respectively
    sugar_weight_remaining = sugar_weight * (1 - 1/5)
    rice_weight_remaining = rice_weight * (1 - 1/3)
    # Calculate the total remaining weight of all items
    total_weight_remaining = sugar_weight_remaining + rice_weight_remaining + 60 # add the weight of green beans
    result = total_weight_remaining
    return result

print(solution())