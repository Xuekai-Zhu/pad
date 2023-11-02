def solution():
    # Calculate the discounted price for the first store
    discount_percent_first_store = 6
    price_first_store = 950
    discount_amount_first_store = (discount_percent_first_store / 100) * price_first_store
    discounted_price_first_store = price_first_store - discount_amount_first_store

    # Calculate the discounted price for the second store
    discount_percent_second_store = 5
    price_second_store = 920
    discount_amount_second_store = (discount_percent_second_store / 100) * price_second_store
    discounted_price_second_store = price_second_store - discount_amount_second_store

    # Calculate the difference in price between the two stores
    price_difference = discounted_price_first_store - discounted_price_second_store
    result = price_difference
    return result

print(solution())