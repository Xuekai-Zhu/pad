def solution():
    # Calculate the total amount paid by both roommates
    total_amount = 757 * 2

    # Calculate the total amount spent on rent and utilities
    rent_utilities_total = 1100 + 114

    # Calculate the amount spent on groceries
    groceries_total = total_amount - rent_utilities_total

    result = groceries_total
    return result

print(solution())