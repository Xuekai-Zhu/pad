def solution():
    """Carrie wants to buy a new iPhone. The new iPhone costs $800. She can trade in her Samsung Galaxy for $240. She can make $80 per week babysitting. How many weeks does she have to work before she can purchase the iPhone?"""
    # Define the cost of the iPhone, the trade-in value of the Samsung Galaxy, and the weekly earnings from babysitting
    iphone_cost = 800
    trade_in_value = 240
    weekly_earnings = 80

    # Calculate the total amount of money Carrie has towards the iPhone
    total_money = trade_in_value

    # Calculate the number of weeks needed to earn the remaining amount
    weeks_needed = (iphone_cost - total_money) / weekly_earnings

    # Round up to the nearest whole number of weeks
    weeks_needed = int(weeks_needed) + (weeks_needed % 1 > 0)

    result = weeks_needed
    return result

print(solution())