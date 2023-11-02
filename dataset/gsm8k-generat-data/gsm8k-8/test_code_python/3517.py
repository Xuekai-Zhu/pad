def solution():
    # Define the cost and quantity of the mixed nuts
    cost = 25
    quantity = 40

    # Calculate the cost per oz of the mixed nuts
    cost_per_oz = cost / quantity

    # Apply the $5 coupon
    cost -= 5

    # Calculate the new cost per oz after the coupon is applied
    new_cost_per_oz = cost / quantity

    # Convert the cost per oz to cents
    cost_per_serving = new_cost_per_oz * 16

    # Return the cost per serving in cents
    return cost_per_serving


# Example usage:
print(solution())  # Output: 13.75 (cents)

print(solution())