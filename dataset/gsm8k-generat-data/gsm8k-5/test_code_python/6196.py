def solution():
    large_order = 3  # Vanessa has sent 3 large orders, each needing 200g of packing peanuts
    packing_peanuts_used = 800  # Vanessa has used a total of 800g of packing peanuts
    large_order_peanuts = large_order * 200  # Total packing peanuts needed for the large orders
    small_order_peanuts = packing_peanuts_used - large_order_peanuts  # Total packing peanuts used for the small orders
    small_orders = small_order_peanuts / 50  # Calculate the number of small orders

    result = small_orders
    return result

print(solution())