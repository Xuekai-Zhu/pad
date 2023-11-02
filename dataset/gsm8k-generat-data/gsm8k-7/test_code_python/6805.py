def solution():
    iphone_price = 800
    iwatch_price = 300
    iphone_discount = 0.15
    iwatch_discount = 0.10
    cashback = 0.02

    # Calculate the discounted price of the iPhone
    iphone_discounted_price = iphone_price * (1 - iphone_discount)

    # Calculate the discounted price of the iWatch
    iwatch_discounted_price = iwatch_price * (1 - iwatch_discount)

    # Calculate the total price before cashback discount
    total_price_before_discount = iphone_discounted_price + iwatch_discounted_price

    # Calculate the cashback amount
    cashback_amount = total_price_before_discount * cashback

    # Calculate the total price after cashback discount
    total_price_after_discount = total_price_before_discount - cashback_amount

    result = total_price_after_discount
    return result

print(solution())