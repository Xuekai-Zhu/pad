def solution():
    # Calculate the total cost of the bread
    total_cost = 3 * 20 * 100

    # Calculate the amount paid with the $20 bills
    paid_amount = 2 * 20 * 100

    # Calculate the change received
    change = 16 * 100

    # Calculate the actual cost of the bread
    actual_cost = paid_amount - change

    # Calculate the cost per slice
    cost_per_slice = actual_cost / (3 * 20)

    # Return the cost per slice in cents
    result = cost_per_slice
    return result

print(solution())