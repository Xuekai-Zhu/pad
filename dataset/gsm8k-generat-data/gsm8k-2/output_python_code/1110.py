def solution():
    """Barbara asked the butcher for 4 1/2 pound steaks that cost $15.00/pound. She also asked for a pound and half of chicken breasts that were $8.00 a pound. How much did she spend at the butchers?"""
    steak_weight = 4.5
    steak_price = 15.00
    chicken_weight = 1.5
    chicken_price = 8.00
    total_price = (steak_weight * steak_price) + (chicken_weight * chicken_price)
    result = total_price
    return result

print(solution())