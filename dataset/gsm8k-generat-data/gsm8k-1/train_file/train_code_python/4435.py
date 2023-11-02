def solution():
    """Mike wants to buy a new phone. The cost of the phone is $1300. How much more money does Mike need if he already has 40% of the amount he needs?"""
    phone_cost = 1300
    current_funds_pct = 40
    current_funds = phone_cost * (current_funds_pct / 100)
    remaining_cost = phone_cost - current_funds
    result = remaining_cost
    return result

print(solution())