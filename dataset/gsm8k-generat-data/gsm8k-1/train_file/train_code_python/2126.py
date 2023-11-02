def solution():
    """Two stores sell the same model of smartphone, but they offer it at different prices and with different discounts. Store A lists the smartphone at a full price of $125 and offers an additional discount of 8%. Store B lists the same smartphone for $130 and offers an additional discount of 10%. After both stores' discounts are applied, how much cheaper is store A's smartphone than store B's smartphone?"""
    store_a_price = 125
    store_a_discount = 0.08
    store_b_price = 130
    store_b_discount = 0.1
    
    store_a_final_price = store_a_price * (1 - store_a_discount)
    store_b_final_price = store_b_price * (1 - store_b_discount)
    
    price_difference = store_b_final_price - store_a_final_price
    
    result = price_difference
    
    return result

print(solution())