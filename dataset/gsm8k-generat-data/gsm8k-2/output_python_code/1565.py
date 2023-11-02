def solution():
    """Two apartment roommates split the rent, utilities, and grocery payments equally each month. The rent for the whole apartment is $1100 and utilities are $114. If one roommate pays $757 in all, how many dollars are groceries for the whole apartment?"""
    total_cost = 1100 + 114 + (757 * 2)  # total cost of rent, utilities, and payments made by both roommates
    groceries_cost = (total_cost) / 2 - (1100 + 114)  # divide total cost in half (since the two roommates split the cost equally) and subtract rent and utilities
    result = groceries_cost
    return result

print(solution())