def solution():
    # Calculate the original cost of a cucumber and a pencil
    original_cost = 20  # Both cucumbers and pencils initially cost $20 each

    # Calculate the number of pencils Isabela bought
    num_pencils = 100 / 2  # Isabela bought twice as many cucumbers as pencils

    # Calculate the discounted price of a pencil
    discounted_price = original_cost * 0.8  # Isabela got a 20% discount on pencils

    # Calculate the total cost of the pencils and cucumbers
    total_cost = (num_pencils * discounted_price) + (100 * original_cost)

    result = total_cost
    return result

print(solution())