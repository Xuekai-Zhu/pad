def solution():
    
    normal_price_per_can = 0.60
    total_cans = 30
    num_paid_cans = total_cans // 2
    total_price = num_paid_cans * normal_price_per_can
    result = total_price
    return result

print(solution())