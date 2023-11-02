def solution():
    
    cups_per_day = 2
    ounces_per_cup = 1.5
    ounces_per_bag = 10.5
    bag_cost = 8
    milk_per_week = 0.5
    milk_cost_per_gallon = 4

    total_ounces = cups_per_day * 7 * ounces_per_cup
    bags_needed = total_ounces / ounces_per_bag
    total_cost_for_coffee = bags_needed * bag_cost
    total_cost_for_milk = milk_per_week * milk_cost_per_gallon
    total_cost = total_cost_for_coffee + total_cost_for_milk
    result = total_cost
    return result

print(solution())