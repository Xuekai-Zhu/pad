def solution():
    
    cups_per_day = 2
    ounces_per_cup = 1.5
    bags_per_week = (cups_per_day * 7 * ounces_per_cup) / 10.5
    cost_per_bag = 8
    cost_per_week_on_coffee = bags_per_week * cost_per_bag
    gallons_per_week = 0.5
    cost_per_gallon = 4
    cost_per_week_on_milk = gallons_per_week * cost_per_gallon
    total_cost_per_week = cost_per_week_on_coffee + cost_per_week_on_milk
    result = total_cost_per_week
    return result

print(solution())