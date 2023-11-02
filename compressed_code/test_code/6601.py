def solution():
    
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