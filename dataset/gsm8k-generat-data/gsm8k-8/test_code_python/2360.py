def solution():
    # Calculate the total cost of all items
    total_cost = 74 + (2 * 2) + 42

    # Calculate the amount exceeding $100
    excess_cost = total_cost - 100

    # Check if there is an excess cost
    if excess_cost > 0:
        # Calculate the discount amount
        discount = excess_cost * 0.10
        # Calculate the total cost with discount applied
        total_cost -= discount

    result = total_cost
    return result

print(solution())