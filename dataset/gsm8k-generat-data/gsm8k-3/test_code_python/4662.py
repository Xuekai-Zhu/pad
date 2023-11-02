def solution():
    """Zach is saving his money to buy a brand new bike that costs $100.  His weekly allowance is $5.  His parent will pay him an extra $10 to mow the lawn.  His neighbor will pay him $7 per hour to babysit their son.  He has already saved up $65.  He'll receive his allowance on Friday and he's planning on babysitting for 2 hours this Saturday after he mows the lawn.  How much more money does Zach need to earn before he can buy the bike?"""
    # Define the cost of the bike and Zach's savings
    BIKE_COST = 100
    SAVINGS = 65

    # Calculate Zach's earnings from mowing the lawn
    lawn_earnings = 10

    # Calculate Zach's earnings from babysitting
    babysitting_earnings = 7 * 2

    # Calculate Zach's total earnings for the week
    total_earnings = SAVINGS + lawn_earnings + babysitting_earnings + 5

    # Calculate how much more money Zach needs to earn to buy the bike
    remaining_cost = BIKE_COST - total_earnings

    # Display how much more money Zach needs to earn
    result = remaining_cost
    return result

print(solution())