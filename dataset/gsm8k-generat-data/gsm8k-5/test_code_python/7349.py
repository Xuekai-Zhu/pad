def solution():
    # Calculate the ratio of sugar to water
    sugar_ratio = 1
    water_ratio = 2
    total_ratio = sugar_ratio + water_ratio

    # Calculate the amount of sugar in one cup of lemonade
    sugar_per_cup = 84 / total_ratio

    # Calculate the total cups of sugar used
    total_sugar_cups = sugar_per_cup * sugar_ratio
    result = total_sugar_cups
    return result

print(solution())