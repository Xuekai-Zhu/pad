def solution():
    num_donuts = 3 * 12
    coffee_per_donut = 2
    coffee_per_pot = 12
    cost_per_pot = 3

    # Calculate the total amount of coffee needed
    total_coffee_needed = num_donuts * coffee_per_donut

    # Calculate the total amount of coffee pots needed
    total_pots_needed = total_coffee_needed / coffee_per_pot

    # Calculate the total cost of all coffee pots needed
    total_cost = total_pots_needed * cost_per_pot
    result = total_cost
    return result

print(solution())