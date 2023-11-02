def solution():
    large_order_peanuts = 200
    small_order_peanuts = 50
    total_peanuts_used = 800
    num_large_orders = 3

    # Calculate the total amount of peanuts used in the small orders
    total_small_orders_peanuts = total_peanuts_used - (num_large_orders * large_order_peanuts)

    # Calculate the number of small orders
    num_small_orders = total_small_orders_peanuts / small_order_peanuts
    result = num_small_orders
    return result

print(solution())