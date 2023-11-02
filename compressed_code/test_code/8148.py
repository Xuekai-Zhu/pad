def solution():
    
    num_shirts = 3
    total_cost = 60
    discount_percent = 40
    discount_amount = total_cost * (discount_percent / 100)
    discounted_cost = total_cost - discount_amount
    cost_per_shirt = discounted_cost / num_shirts
    result = cost_per_shirt
    return result

print(solution())