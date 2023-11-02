def solution():
    
    rent = 1100
    utilities = 114
    total_cost = rent + utilities
    roommate_share = total_cost / 2
    groceries = 757 - roommate_share
    result = groceries * 2
    return result

print(solution())