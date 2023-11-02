def solution():
    
    donuts_per_dozen = 12
    total_donuts = 3 * donuts_per_dozen
    coffee_per_donut = 2
    coffee_needed = total_donuts * coffee_per_donut
    coffee_per_pot = 12
    pots_needed = coffee_needed / coffee_per_pot
    cost_per_pot = 3
    total_cost = pots_needed * cost_per_pot
    result = total_cost
    return result

print(solution())