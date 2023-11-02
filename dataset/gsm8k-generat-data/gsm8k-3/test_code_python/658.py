def solution():
    """Sara is checking out two different stores to buy a computer. The first store offers a device for $950 with a 6% discount. The second sells the same computer for €920 with a 5% discount. What is the difference in price between the two stores?"""
    # Find the discounted price at the first store
    discount_percent = 6
    original_price = 950
    discount_amount = original_price * (discount_percent / 100)
    discounted_price_1 = original_price - discount_amount

    # Find the discounted price at the second store
    discount_percent = 5
    original_price = 920
    discount_amount = original_price * (discount_percent / 100)
    discounted_price_2 = original_price - discount_amount

    # Find the difference in price between the two stores
    price_difference = discounted_price_1 - discounted_price_2

    # Display the price difference
    result = price_difference
    return result

print(solution())