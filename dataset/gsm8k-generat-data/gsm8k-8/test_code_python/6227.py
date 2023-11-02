def solution():
    # Define the package weight in pounds
    package_weight = 5

    # Calculate the shipping cost based on weight
    shipping_cost = 0.8 * package_weight

    # Add the flat fee to the weight-based cost
    total_cost = shipping_cost + 5

    result = total_cost
    return result

print(solution())