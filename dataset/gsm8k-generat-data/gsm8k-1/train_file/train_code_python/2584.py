def solution():
    """Rookie police officers have to buy duty shoes at the full price of $85, but officers who have served at least a year get a 20% discount. Officers who have served at least three years get an additional 25% off the discounted price. How much does an officer who has served at least three years have to pay for shoes?"""
    full_price = 85
    discount_1 = 0.2
    discount_2 = 0.25
    final_price = full_price * (1 - discount_1) * (1 - discount_2)
    result = final_price
    return result

print(solution())