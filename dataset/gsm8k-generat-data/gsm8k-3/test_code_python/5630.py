def solution():
    """Sara got her first paycheck of two weeks of work. She had worked 40 hours a week at $11.50 per hour. The first thing she did was buy a new set of tires for her car for $410. How much money was she left with?"""
    # Define the rate per hour
    HOURLY_RATE = 11.50

    # Calculate the total earnings
    total_earnings = 40 * 2 * HOURLY_RATE

    # Subtract the cost of the new set of tires
    left_over = total_earnings - 410

    # Display the amount of money Sara was left with
    result = left_over
    return result

print(solution())