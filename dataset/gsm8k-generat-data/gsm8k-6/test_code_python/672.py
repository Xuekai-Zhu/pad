def solution():
    # Calculate the number of pounds of carrots per year
    pounds_per_carrot = 1/5  # 1 carrot is 1/5 pound
    pounds_per_year = 365 * pounds_per_carrot  # 365 days in a year
    # Calculate the cost of carrots per year
    cost_per_bag = 2.00  # cost of 1 bag of carrots
    bags_per_year = pounds_per_year / 5  # 5 pounds per bag
    cost_per_year = bags_per_year * cost_per_bag
    result = cost_per_year
    return result

print(solution())