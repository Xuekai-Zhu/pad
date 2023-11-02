def solution():
    """Dexter went to the mall and saw that Apple products are on sale. He wants to buy an iPhone 12 with a 15% discount and an iWatch with a 10% discount. The price tag shows that an iPhone 12 costs $800 while an iWatch costs $300. Upon check out, he will receive a further 2% cashback discount. How much would the items cost in total after the discount and cashback?"""
    iphone_cost = 800
    iwatch_cost = 300
    iphone_discount = 0.15
    iwatch_discount = 0.1
    iphone_discounted_price = iphone_cost * (1 - iphone_discount)
    iwatch_discounted_price = iwatch_cost * (1 - iwatch_discount)
    total_cost = iphone_discounted_price + iwatch_discounted_price
    cashback = 0.02
    total_cost_after_cashback = total_cost * (1 - cashback)
    result = total_cost_after_cashback
    return result

print(solution())