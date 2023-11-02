def solution():
    cost_of_seeds = 50
    cost_of_fertilizers_and_pesticides = 35
    cost_of_labor = 15
    total_cost = cost_of_seeds + cost_of_fertilizers_and_pesticides + cost_of_labor
    profit_percent = 10/100
    total_profit = total_cost * profit_percent + total_cost
    num_of_bags = 10
    cost_per_bag = total_profit / num_of_bags
    result = cost_per_bag
    return result

print(solution())