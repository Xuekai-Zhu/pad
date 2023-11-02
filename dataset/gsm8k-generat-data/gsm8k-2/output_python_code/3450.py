def solution():
    """Lyla, a grocery store owner, bought rice weighing 30 kg less than green beans, which weigh 10 kg more than sugar. While carrying the goods to the store, the bags fell down and 1/3 weight of the rice and 1/5 weight of sugar was lost. If the green beans weighed 60 kgs, then how much did the remaining stock weigh?"""
    green_beans_weight = 60
    sugar_weight = green_beans_weight - 10
    rice_weight = sugar_weight - 30
    rice_loss = rice_weight * (1/3)
    sugar_loss = sugar_weight * (1/5)
    remaining_weight = green_beans_weight - rice_loss - sugar_loss
    result = remaining_weight
    return result

print(solution())