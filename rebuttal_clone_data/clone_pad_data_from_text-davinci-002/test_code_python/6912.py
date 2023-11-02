def solution():
    total_cans = 9
    cans_with_coupons = 5
    total_cost = 20
    total_change = 5.50
    
    cost_per_can = (total_cost - total_change) / (total_cans - cans_with_coupons)
    result = cost_per_can * 100
    
    return result

print(solution())