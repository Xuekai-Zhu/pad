def solution():
    """Whenever Katie and her family eat donuts, they need some coffee to dunk them in. She notices that for each donut they need 2 ounces of coffee. Every pot of coffee she makes contains 12 ounces and costs $3 to make. If her family finishes 3 dozen donuts, how much do they spend on coffee?"""
    donut_count = 36
    coffee_per_donut = 2
    coffee_per_pot = 12
    pots_needed = (donut_count * coffee_per_donut) // coffee_per_pot + 1
    cost_per_pot = 3
    total_cost = pots_needed * cost_per_pot
    result = total_cost
    return result

print(solution())