def solution():
    
    store_a_price = 125
    store_a_discount = 0.08
    store_b_price = 130
    store_b_discount = 0.1
    store_a_final_price = store_a_price - (store_a_price * store_a_discount)
    store_b_final_price = store_b_price - (store_b_price * store_b_discount)
    difference = store_b_final_price - store_a_final_price
    result = difference
    return result

print(solution())