def solution():
    """James decides to buy a living room set. The coach cost $2500 and the sectional cost $3500 and everything else has a combined cost of $2000. He gets a 10% discount on everything. How much did he pay?"""
    couch_cost = 2500
    sectional_cost = 3500
    other_cost = 2000
    total_cost = couch_cost + sectional_cost + other_cost
    discount_rate = 10
    discount_amount = total_cost * (discount_rate / 100)
    total_cost_discounted = total_cost - discount_amount
    result = total_cost_discounted
    
    return result

print(solution())