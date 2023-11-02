def solution():
    rent = 1100
    utilities = 114
    roommate_payment = 757
    total_payment = rent + utilities + groceries
    groceries = total_payment - (rent + utilities)
    result = groceries
    return result

print(solution())