def solution():
    """Mildred and Candice went to the market. Mildred spent $25 while Candice spent $35. If their mom gave them $100 to spend, how much will be left with them after spending?"""
    initial_amount = 100
    mildred_spent = 25
    candice_spent = 35
    total_spent = mildred_spent + candice_spent
    remaining_amount = initial_amount - total_spent
    result = remaining_amount
    return result

print(solution())