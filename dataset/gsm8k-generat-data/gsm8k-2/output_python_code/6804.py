def solution():
    """Dexter went to the mall and saw that Apple products are on sale. He wants to buy an iPhone 12 with a 15% discount and an iWatch with a 10% discount. The price tag shows that an iPhone 12 costs $800 while an iWatch costs $300. Upon check out, he will receive a further 2% cashback discount. How much would the items cost in total after the discount and cashback?"""
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