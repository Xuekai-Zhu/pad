def solution():
    """Carly is overnight shipping some fresh-baked cookies to her grandma. The shipping cost is equal to a flat $5.00 fee plus $0.80 per pound of weight. If the package weighs 5 pounds, how much does Carly pay for shipping?"""
    # Define the weight of the package in pounds
    package_weight = 5

    # Calculate the shipping cost based on the weight
    shipping_cost = 5.00 + (0.80 * package_weight)

    # Return the result
    result = shipping_cost
    return result

print(solution())