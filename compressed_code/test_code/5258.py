def solution():
    
    iphone_price = 800
    iwatch_price = 300
    iphone_discount = 0.15
    iwatch_discount = 0.1
    cashback_discount = 0.02

    iphone_discounted_price = iphone_price * (1 - iphone_discount)
    iwatch_discounted_price = iwatch_price * (1 - iwatch_discount)

    total_price = iphone_discounted_price + iwatch_discounted_price
    cashback_amount = total_price * cashback_discount
    total_price_after_cashback = total_price - cashback_amount

    result = total_price_after_cashback
    return result

print(solution())