def solution():
    # Calculate the weight of sugar
    sugar_weight = 60 - 10  # Green beans weigh 10 kg more than sugar
    # Calculate the weight of green beans
    green_beans_weight = 60
    # Calculate the weight of rice
    rice_weight = green_beans_weight - 30  # Rice weighs 30 kg less than green beans
    # Calculate the weight of rice and sugar after the bags fell down
    rice_weight = rice_weight - (1/3 * rice_weight)
    sugar_weight = sugar_weight - (1/5 * sugar_weight)
    # Calculate the remaining stock weight
    remaining_weight = rice_weight + sugar_weight + green_beans_weight
    result = remaining_weight
    return result

print(solution())