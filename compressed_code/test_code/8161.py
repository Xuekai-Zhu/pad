def solution():
    
    item_cost = 200
    num_items = 7
    total_cost = item_cost * num_items
    discount_threshold = 1000
    discount_rate = 0.1
    
    if total_cost > discount_threshold:
        amount_over_threshold = total_cost - discount_threshold
        discount_amount = amount_over_threshold * discount_rate
        total_cost -= discount_amount
    
    result = total_cost
    return result

print(solution())