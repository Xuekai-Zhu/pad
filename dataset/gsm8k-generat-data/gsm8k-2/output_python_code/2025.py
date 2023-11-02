def solution():
    """Inez has $150. She spends one-half on hockey skates and a certain amount on hockey pads. If Inez has $25 remaining, how much did the hockey pads cost, together, in dollars?"""
    total_money = 150
    remaining_money = 25
    skates_cost = total_money / 2
    pads_cost = total_money - skates_cost - remaining_money
    result = pads_cost
    return result

print(solution())