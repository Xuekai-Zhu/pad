def solution():
    store_a_price = 125
    store_a_discount = 0.08
    store_b_price = 130
    store_b_discount = 0.1

    # Calculate the final price of the smartphone at store A
    store_a_final_price = store_a_price * (1 - store_a_discount)

    # Calculate the final price of the smartphone at store B
    store_b_final_price = store_b_price * (1 - store_b_discount)

    # Calculate the price difference between store A's smartphone and store B's smartphone
    price_difference = store_b_final_price - store_a_final_price
    result = price_difference
    return result

print(solution())