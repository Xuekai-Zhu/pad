def solution():
    
    phone_cost = 1300
    current_funds_pct = 40
    current_funds = phone_cost * (current_funds_pct / 100)
    remaining_cost = phone_cost - current_funds
    result = remaining_cost
    return result

print(solution())