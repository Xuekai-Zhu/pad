def solution():
    """Sara got her first paycheck of two weeks of work. She had worked 40 hours a week at $11.50 per hour. The first thing she did was buy a new set of tires for her car for $410. How much money was she left with?"""
    # Define the number of hours worked per week and the hourly wage
    hours_per_week = 40
    hourly_wage = 11.5

    # Calculate the total earnings before taxes
    total_earnings = hours_per_week * hourly_wage * 2

    # Subtract the cost of the new tires
    money_left = total_earnings - 410

    result = money_left
    return result

print(solution())