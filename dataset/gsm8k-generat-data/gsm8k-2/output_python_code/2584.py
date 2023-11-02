def solution():
    """Rookie police officers have to buy duty shoes at the full price of $85, but officers who have served at least a year get a 20% discount. Officers who have served at least three years get an additional 25% off the discounted price. How much does an officer who has served at least three years have to pay for shoes?"""
    full_price = 85
    discount_year = 1
    discount_percentage = 0.2
    additional_discount_year = 3
    additional_discount_percentage = 0.25
    if additional_discount_year >= 3:
        discount_percentage += additional_discount_percentage

    discounted_price = full_price - (discount_percentage * full_price)
    result = discounted_price
    return result

print(solution())