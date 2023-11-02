def solution():
    # Calculate the total cost of the original order
    original_order_cost = 2 * 3 + 2 * 2 + 2 * 2

    # Add the cost of tax to the original order cost
    total_cost = original_order_cost + 1

    # Calculate the cost of Ben's additional order items
    additional_pancakes_cost = 2
    additional_cocoa_cost = 2

    # Add the cost of Ben's additional order items to the total cost
    total_cost += additional_pancakes_cost + additional_cocoa_cost

    # Calculate the amount of change from $15
    change = float(15 - total_cost)
    result = change
    return result

print(solution())