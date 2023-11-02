def solution():
    """Michael has $50. He wants to surprise his mom on Mother's day by buying a cake for $20, a bouquet for $36, and a set of balloons for $5. How much more money does Michael need to buy all those?"""
    total_cost = 20 + 36 + 5
    current_balance = 50
    remaining_balance = current_balance - total_cost
    result = remaining_balance
    return result

print(solution())