def solution():
    # Define variables
    donuts = 3 * 12
    coffee_per_donut = 2
    coffee_per_pot = 12
    cost_per_pot = 3

    # Calculate the total amount of coffee needed
    total_coffee = donuts * coffee_per_donut

    # Calculate the total number of pots needed
    num_pots = total_coffee / coffee_per_pot
    num_pots = int(num_pots) + 1 if num_pots % 1 != 0 else int(num_pots)

    # Calculate the total cost of the coffee
    total_cost = num_pots * cost_per_pot

    return total_cost

print(solution())