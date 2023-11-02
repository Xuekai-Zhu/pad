def solution():
    """Carrie wants to buy a new iPhone. The new iPhone costs $800. She can trade in her Samsung Galaxy for $240. She can make $80 per week babysitting. How many weeks does she have to work before she can purchase the iPhone?"""
    # Define the cost of the iPhone and the trade-in value of the Samsung Galaxy
    IPHONE_COST = 800
    GALAXY_TRADE_IN_VALUE = 240

    # Calculate the total amount Carrie can put towards the iPhone
    total_amount = GALAXY_TRADE_IN_VALUE  # start with trade-in value
    # Add the amount she can make babysitting each week
    weeks = 0
    while total_amount < IPHONE_COST:
        weeks += 1
        total_amount += 80

    # Display the number of weeks Carrie needs to work
    result = weeks
    return result

print(solution())