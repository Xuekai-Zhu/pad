def solution():
    """James decides to buy a living room set. The coach cost $2500 and the sectional cost $3500 and everything else has a combined cost of $2000. He gets a 10% discount on everything. How much did he pay?"""
    coach_cost = 2500
    sectional_cost = 3500
    other_cost = 2000
    total_cost = coach_cost + sectional_cost + other_cost
    discount = 0.1 * total_cost
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())