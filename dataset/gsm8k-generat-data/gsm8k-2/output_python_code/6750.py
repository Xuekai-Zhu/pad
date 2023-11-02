def solution():
    """After buying shirts worth $27 from a store, Dennis received 2 $10 bills and $3 in loose coins for his change. How much money did Dennis have initially?"""
    total_change = 2*10 + 3
    initial_money = 27 + total_change
    result = initial_money
    return result

print(solution())