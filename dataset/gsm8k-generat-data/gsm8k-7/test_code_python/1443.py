def solution():
    full_price = 125.00
    discount_percentage = 0.20  # 20% discount
    coupon_value = 10.00
    credit_card_discount_percentage = 0.10  # 10% discount

    # Calculate the discounted price after the first discount
    discounted_price = full_price * (1 - discount_percentage)

    # Subtract the coupon value from the discounted price
    discounted_price -= coupon_value

    # Calculate the final price after the credit card discount
    final_price = discounted_price * (1 - credit_card_discount_percentage)

    # Calculate the amount saved compared to the full price
    amount_saved = full_price - final_price
    result = amount_saved
    return result

print(solution())