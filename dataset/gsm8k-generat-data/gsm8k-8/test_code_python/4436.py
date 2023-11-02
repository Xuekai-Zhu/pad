def solution():
    phone_cost = 1300
    current_funds_percentage = 0.4
    current_funds = current_funds_percentage * phone_cost
    remaining_funds = phone_cost - current_funds
    result = remaining_funds
    return result

print(solution())