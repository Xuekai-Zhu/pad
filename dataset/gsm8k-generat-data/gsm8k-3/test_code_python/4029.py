def solution():
    """To raise money, a school is selling ice-pops for $1.50. It costs 90 cents to make each pop, and the money from the pops will be used to buy pencils, which cost $1.80 each. How many pops must be sold to buy 100 pencils?"""
    # Define the selling price and cost per pop
    SELLING_PRICE = 1.5
    COST_PER_POP = 0.9

    # Define the cost of one pencil
    PENCIL_COST = 1.8

    # Calculate the profit per pop
    profit_per_pop = SELLING_PRICE - COST_PER_POP

    # Calculate the number of pops required to buy 100 pencils
    pops_required = 100 * PENCIL_COST / profit_per_pop

    # Round up to the nearest integer
    pops_required = math.ceil(pops_required)

    # Display the number of pops required
    result = pops_required
    return result

print(solution())