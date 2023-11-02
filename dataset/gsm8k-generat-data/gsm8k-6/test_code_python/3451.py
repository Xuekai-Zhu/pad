def solution():
    # Calculate the weight of sugar
    sugar_weight = (60 - 10) - 30  # green beans weigh 10 kg more than sugar, and rice weighs 30 kg less than green beans
    # Calculate the weight of rice after losing 1/3 of its weight
    rice_weight = (2/3) * (sugar_weight - 30)  
    # Calculate the weight of sugar after losing 1/5 of its weight
    sugar_weight = (4/5) * sugar_weight  
    # Calculate the weight of remaining stock
    remaining_weight = green_beans_weight + rice_weight + sugar_weight  
    result = remaining_weight
    return result

print(solution())