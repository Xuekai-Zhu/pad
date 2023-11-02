def solution():
    """Two apartment roommates split the rent, utilities, and grocery payments equally each month. The rent for the whole apartment is $1100 and utilities are $114. If one roommate pays $757 in all, how many dollars are groceries for the whole apartment?"""
    # Define the total cost of rent and utilities
    rent_and_utilities = 1100 + 114

    # Calculate the total cost paid by both roommates
    total_cost = 757 * 2

    # Determine the cost of groceries
    groceries = (total_cost - rent_and_utilities) / 2

    result = groceries
    return result

print(solution())