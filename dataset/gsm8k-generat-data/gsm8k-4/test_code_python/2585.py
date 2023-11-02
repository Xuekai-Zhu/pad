def solution():
    """Rookie police officers have to buy duty shoes at the full price of $85, but officers who have served at least a year get a 20% discount. Officers who have served at least three years get an additional 25% off the discounted price. How much does an officer who has served at least three years have to pay for shoes?"""
    # Define the initial price of the shoes
    initial_price = 85

    # Calculate the price for officers who have served at least one year
    one_year_discount = initial_price * 0.2
    one_year_price = initial_price - one_year_discount

    # Calculate the price for officers who have served at least three years
    three_year_discount = one_year_price * 0.25
    three_year_price = one_year_price - three_year_discount

    result = three_year_price
    return result

print(solution())