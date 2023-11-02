def solution():
    original_price = None
    discounted_price = 14.50
    discount1 = 0.5  # 50% summer discount
    discount2 = 10.0  # $10 Wednesday discount for jeans

    # Calculate the price after the summer discount
    price_after_summer_discount = discounted_price / (1 - discount1)

    # Check if today is Wednesday and apply the additional discount if so
    today_is_wednesday = True  # Assume today is Wednesday for testing purposes
    if today_is_wednesday:
        price_after_wednesday_discount = price_after_summer_discount - discount2
    else:
        price_after_wednesday_discount = price_after_summer_discount

    # Calculate the original price before all discounts
    original_price = price_after_wednesday_discount / (1 - discount1)
    result = original_price
    return result

print(solution())