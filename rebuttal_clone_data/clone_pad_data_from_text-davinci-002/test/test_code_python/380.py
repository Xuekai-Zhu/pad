def solution():
    carrots_per_day = 1
    days_in_year = 365
    carrots_in_bag = 5
    bags_per_year = carrots_per_day / carrots_in_bag * days_in_year
    cost_per_bag = 2.00
    total_cost = bags_per_year * cost_per_bag
    result = total_cost
    return result

print(solution())