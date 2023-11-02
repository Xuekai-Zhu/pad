def solution():
    
    bottles_per_year = 12
    cost_per_bottle = 30
    discount_percent = 30
    cost_before_discount = bottles_per_year * cost_per_bottle
    discount_amount = cost_before_discount * (discount_percent / 100)
    cost_after_discount = cost_before_discount - discount_amount
    result = cost_after_discount
    return result

print(solution())