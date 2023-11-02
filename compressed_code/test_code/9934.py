def solution():
    
    initial_price = 40
    tax_rate = 0.05
    discount = 8
    price_after_tax = initial_price * (1 + tax_rate)
    final_price = price_after_tax - discount
    cody_payment = final_price / 2
    result = cody_payment
    return result

print(solution())