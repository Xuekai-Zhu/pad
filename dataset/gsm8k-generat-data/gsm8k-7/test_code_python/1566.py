def solution():
    rent = 1100
    utilities = 114
    total_cost = rent + utilities

    # Calculate the total cost paid by both roommates
    total_paid = 2 * 757

    # Calculate the total cost of groceries
    groceries_cost = total_paid - total_cost
    result = groceries_cost
    return result

print(solution())