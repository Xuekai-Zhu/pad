def solution():
    """Rookie police officers have to buy duty shoes at the full price of $85, but officers who have served at least a year get a 20% discount. Officers who have served at least three years get an additional 25% off the discounted price. How much does an officer who has served at least three years have to pay for shoes?"""
    # Define the full price and discount percentages
    FULL_PRICE = 85
    DISCOUNT_1 = 0.2
    DISCOUNT_2 = 0.25

    # Calculate the discounted price for officers who have served at least a year
    discount_price_1 = FULL_PRICE * (1 - DISCOUNT_1)

    # Calculate the discounted price for officers who have served at least three years
    discount_price_2 = discount_price_1 * (1 - DISCOUNT_2)

    # Display the final price an officer who has served at least three years has to pay for shoes
    result = discount_price_2
    return result

print(solution())