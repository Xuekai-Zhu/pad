def solution():
    """Inez has $150. She spends one-half on hockey skates and a certain amount on hockey pads. If Inez has $25 remaining, how much did the hockey pads cost, together, in dollars?"""
    starting_funds = 150
    remaining_funds = 25
    skates_cost = starting_funds / 2
    pads_cost = starting_funds - skates_cost - remaining_funds
    total_cost = pads_cost * 2
    result = total_cost
    return result

print(solution())