def solution():
    
    bag_cost = 25
    bag_size = 40
    coupon_amount = 5
    total_cost = bag_cost - coupon_amount
    cost_per_oz = total_cost / bag_size
    cost_per_serving = cost_per_oz * 1 * 100 
    result = cost_per_serving
    return result

print(solution())