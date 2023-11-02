def solution():
    num_shirts = 3
    original_price = 60
    discount_percent = 0.4  # 40% discount

    # Calculate the total price of all shirts before the discount
    total_original_price = num_shirts * original_price

    # Calculate the total discount amount
    total_discount = total_original_price * discount_percent

    # Calculate the total price of all shirts after the discount
    total_discounted_price = total_original_price - total_discount

    # Calculate the price per shirt after the discount
    price_per_shirt = total_discounted_price / num_shirts
    result = price_per_shirt
    return result

print(solution())