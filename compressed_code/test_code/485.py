def solution():
    
    first_store_price = 950
    first_store_discount = 0.06
    second_store_price = 920
    second_store_discount = 0.05

    first_store_discount_amount = first_store_price * first_store_discount
    first_store_final_price = first_store_price - first_store_discount_amount

    second_store_discount_amount = second_store_price * second_store_discount
    second_store_final_price = second_store_price - second_store_discount_amount

    difference = first_store_final_price - second_store_final_price
    result = difference
    return result

print(solution())