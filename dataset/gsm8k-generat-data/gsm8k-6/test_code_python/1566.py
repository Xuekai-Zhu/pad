def solution():
    # Calculate the total amount paid for rent and utilities
    rent_and_utilities = 1100 + 114

    # Calculate the total amount paid by both roommates
    total_paid = 757 * 2

    # Calculate the amount paid for groceries
    groceries = (total_paid - rent_and_utilities) / 2

    result = groceries
    return result

print(solution())