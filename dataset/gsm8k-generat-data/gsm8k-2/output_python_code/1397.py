def solution():
    """Charlotte needs to know how much money to have with her when she goes to the shoe store. How much money should Charlotte bring to buy a pair of boots, if the original price is $90 and there is a discount of 20%?"""
    original_price = 90
    discount = 0.2
    discounted_price = original_price - (original_price * discount)
    result = discounted_price
    return result

print(solution())