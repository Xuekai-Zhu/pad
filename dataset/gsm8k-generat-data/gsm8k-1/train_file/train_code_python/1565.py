def solution():
    """Two apartment roommates split the rent, utilities, and grocery payments equally each month. The rent for the whole apartment is $1100 and utilities are $114. If one roommate pays $757 in all, how many dollars are groceries for the whole apartment?"""
    rent = 1100
    utilities = 114
    total_cost = rent + utilities
    roommate_share = total_cost / 2
    groceries = 757 - roommate_share
    result = groceries * 2
    return result

print(solution())