def solution():
    # Calculate the cost of the stockings before the discount
    stockings_cost = 5 * 9 * 20

    # Calculate the discount
    discount = 0.1

    # Apply the discount
    discounted_cost = stockings_cost * (1 - discount)

    # Calculate the total cost with monogramming
    total_cost = discounted_cost + (9 * 5)

    result = total_cost
    return result

print(solution())