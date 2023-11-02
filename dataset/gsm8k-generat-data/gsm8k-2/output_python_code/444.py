def solution():
    """Carla bought 2 bags of mini peanut butter cups on clearance. Each bag was $6.00 but was 75% off. How much did she spend on 2 bags of candy?"""
    original_price = 6.00
    discount = 0.75
    sale_price = original_price * (1 - discount)
    total_price = sale_price * 2
    result = total_price
    return result

print(solution())