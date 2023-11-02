def solution():
    
    large_order_peanuts = 200
    small_order_peanuts = 50
    total_peanuts_used = 800
    total_large_orders = 3
    peanuts_from_large_orders = total_large_orders * large_order_peanuts
    peanuts_from_small_orders = total_peanuts_used - peanuts_from_large_orders
    number_of_small_orders = peanuts_from_small_orders / small_order_peanuts
    result = number_of_small_orders
    return result

print(solution())