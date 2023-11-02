def solution():
    store1_original_price = 950
    store1_discount = 6
    store1_sale_price = store1_original_price - (store1_original_price * (store1_discount / 100))
    
    store2_original_price = 920
    store2_discount = 5
    store2_sale_price = store2_original_price - (store2_original_price * (store2_discount / 100))
    
    price_difference = store1_sale_price - store2_sale_price
    result = price_difference
    return result

print(solution())