def solution():
    normal_cost = 200
    discount_cost = normal_cost * 0.3
    visits = 2
    total_discount_cost = discount_cost * visits
    total_normal_cost = normal_cost * visits
    savings = total_normal_cost - total_discount_cost
    result = savings
    
    return result

print(solution())