def solution():
    """Sara is checking out two different stores to buy a computer. The first store offers a device for $950 with a 6% discount. The second sells the same computer for €920 with a 5% discount. What is the difference in price between the two stores?"""
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