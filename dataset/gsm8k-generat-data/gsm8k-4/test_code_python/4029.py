def solution():
    """To raise money, a school is selling ice-pops for $1.50. It costs 90 cents to make each pop, and the money from the pops will be used to buy pencils, which cost $1.80 each. How many pops must be sold to buy 100 pencils?"""
    # Define the selling price and cost of making each ice-pop
    selling_price = 1.5
    making_cost = 0.9

    # Define the cost of each pencil
    pencil_cost = 1.8

    # Calculate the profit per ice-pop
    profit_per_pop = selling_price - making_cost

    # Calculate the number of ice-pops needed to buy 100 pencils
    pops_needed = 100 * pencil_cost / profit_per_pop

    # Round up to the nearest whole number of ice-pops
    result = int(pops_needed) + 1
    return result

print(solution())