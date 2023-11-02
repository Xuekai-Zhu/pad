def solution():
    """Carly is overnight shipping some fresh-baked cookies to her grandma. The shipping cost is equal to a flat $5.00 fee plus $0.80 per pound of weight. If the package weighs 5 pounds, how much does Carly pay for shipping?"""
    # Define the cost per pound and the flat fee
    COST_PER_POUND = 0.8
    FLAT_FEE = 5.0

    # Define the weight of the package
    weight = 5

    # Calculate the total shipping cost
    total_cost = FLAT_FEE + (COST_PER_POUND * weight)

    # Display the total cost
    result = total_cost
    return result

print(solution())