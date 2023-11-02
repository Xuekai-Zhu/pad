def solution():
    total_cost = 1100 + 114  # Total cost of rent and utilities
    roommate_share = 757  # One roommate pays $757 in all

    # Calculate the total amount paid by both roommates
    total_paid = roommate_share * 2

    # Calculate the cost of groceries
    grocery_cost = total_paid - total_cost
    result = grocery_cost
    return result

print(solution())