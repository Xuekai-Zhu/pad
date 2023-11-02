def solution():
    total_gold = 100
    ratio = 1/4  # For every unit of gold Greg has, Katie has 4 units

    total_ratio = ratio + 1  # The total ratio is the sum of the ratios for Greg and Katie
    greg_ratio = ratio / total_ratio  # The part of the total ratio that represents Greg's gold
    greg_gold = greg_ratio * total_gold

    result = greg_gold
    return result

print(solution())