def solution():
    """In November, a toy was $40. In December, the price increased by 80%. In January, the price decreased by 50%. What was the price of the toy after it was discounted in January?"""
    november_price = 40
    december_increase = 80
    january_decrease = 50
    december_price = november_price * (1 + (december_increase / 100))
    january_price = december_price * (1 - (january_decrease / 100))
    result = january_price
    return result

print(solution())