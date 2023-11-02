def solution():
    coffee_price = 6
    cheesecake_price = 10
    discount = 0.25  # 25% discount

    # Calculate the total price without discount
    total_price_no_discount = coffee_price + cheesecake_price

    # Calculate the discount amount
    discount_amount = total_price_no_discount * discount

    # Calculate the total price after discount
    total_price_after_discount = total_price_no_discount - discount_amount

    result = total_price_after_discount
    return result

print(solution())