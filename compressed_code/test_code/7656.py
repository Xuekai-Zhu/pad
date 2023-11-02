def solution():
    
    shoes_cost = 74
    socks_cost = 2 * 2
    bag_cost = 42
    total_cost = shoes_cost + socks_cost + bag_cost
    discount_threshold = 100
    if total_cost > discount_threshold:
        discount_amount = (total_cost - discount_threshold) * 0.1
        discounted_total = total_cost - discount_amount
        result = discounted_total
    else:
        result = total_cost
    
    return result

print(solution())