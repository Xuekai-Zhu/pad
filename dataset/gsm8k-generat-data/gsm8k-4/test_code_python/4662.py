def solution():
    """Zach is saving his money to buy a brand new bike that costs $100. His weekly allowance is $5.
    His parent will pay him an extra $10 to mow the lawn. His neighbor will pay him $7 per hour to babysit their son.
    He has already saved up $65. He'll receive his allowance on Friday and he's planning on babysitting for 2 hours
    this Saturday after he mows the lawn. How much more money does Zach need to earn before he can buy the bike?"""
    # Define the cost of the bike and Zach's current savings
    BIKE_COST = 100
    CURRENT_SAVINGS = 65

    # Define the amount Zach can earn from mowing the lawn and babysitting
    LAWN_MOWING = 10
    BABYSITTING_HOURLY_RATE = 7

    # Define Zach's expected earnings from babysitting and lawn mowing
    expected_earnings = CURRENT_SAVINGS + LAWN_MOWING

    # Add Zach's expected earnings from babysitting to his expected earnings
    expected_earnings += BABYSITTING_HOURLY_RATE * 2

    # Add Zach's allowance to his expected earnings
    expected_earnings += 5
     
    # Calculate the remaining amount Zach needs to earn to buy the bike
    remaining_amount = BIKE_COST - expected_earnings

    result = remaining_amount
    return result

print(solution())