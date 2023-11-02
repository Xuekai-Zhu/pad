def solution():
    """ Cody goes to the store and buys $40 worth of stuff. The taxes were 5%. After taxes, he got an $8 discount. Cody and his friend split the final price equally. How much did Cody pay?"""
    initial_price = 40
    tax_rate = 0.05
    discount = 8
    price_after_tax = initial_price * (1 + tax_rate)
    final_price = price_after_tax - discount
    cody_payment = final_price / 2
    result = cody_payment
    return result

print(solution())