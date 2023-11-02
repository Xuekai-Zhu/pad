def solution():
    
    original_cost = 50
    discount_percent = 30
    discount_amount = original_cost * (discount_percent / 100)
    final_cost = original_cost - discount_amount
    result = final_cost
    return result

print(solution())