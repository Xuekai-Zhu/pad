def solution():
    # Calculate the total amount of packing peanuts used for large orders
    large_orders_peanuts = 3 * 200  # each large order needs 200g of packing peanuts

    # Calculate the amount of packing peanuts used for small orders
    small_orders_peanuts = 800 - large_orders_peanuts

    # Calculate the number of small orders
    small_orders = small_orders_peanuts / 50  # each small order needs 50g of packing peanuts

    result = small_orders
    return result

print(solution())