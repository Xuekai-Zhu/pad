def solution():
    """Two stores sell the same model of smartphone, but they offer it at different prices and with different discounts. Store A lists the smartphone at a full price of $125 and offers an additional discount of 8%. Store B lists the same smartphone for $130 and offers an additional discount of 10%. After both stores' discounts are applied, how much cheaper is store A's smartphone than store B's smartphone?"""
    # Define the initial prices and discounts
    STORE_A_PRICE = 125
    STORE_A_DISCOUNT = 0.08
    STORE_B_PRICE = 130
    STORE_B_DISCOUNT = 0.1

    # Calculate the final price of the smartphone at each store
    store_a_final_price = STORE_A_PRICE * (1 - STORE_A_DISCOUNT)
    store_b_final_price = STORE_B_PRICE * (1 - STORE_B_DISCOUNT)

    # Calculate the price difference
    price_difference = store_b_final_price - store_a_final_price

    # Display the price difference
    result = price_difference
    return result

print(solution())