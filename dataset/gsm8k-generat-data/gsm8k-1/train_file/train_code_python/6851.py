def solution():
    """Mark has the option of getting a $300 lens with a 20% discount or a $220 lens. How much money does he save by buying the cheaper lens?"""
    discount = 0.2
    lens1_price = 300
    lens2_price = 220
    lens1_discounted_price = lens1_price - (discount * lens1_price)
    if lens1_discounted_price < lens2_price:
        saved_money = lens2_price - lens1_discounted_price
    else:
        saved_money = 0
    result = saved_money
    return result

print(solution())