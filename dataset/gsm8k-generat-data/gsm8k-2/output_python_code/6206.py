def solution():
    """On a mall-wide sale, Andre bought a $1350 treadmill for a 30% discount and 2 pieces of 45-pound plates for $50 each. How much did Andre pay for the treadmill and plates?"""
    treadmill_price = 1350
    discount_percentage = 30
    discount_amount = treadmill_price * (discount_percentage / 100)
    discounted_price = treadmill_price - discount_amount
    plates_price = 2 * 50
    total_price = discounted_price + plates_price
    result = total_price
    return result

print(solution())