def solution():
    """Zainab earns $2 an hour passing out flyers at the town square. She passes out flyers on Monday, Wednesday, and Saturday each week, for 4 hours at a time. After passing out flyers for 4 weeks, how much money will Zainab earn?"""
    # Define Zainab's rate per hour
    RATE = 2

    # Define the number of hours worked each week
    hours_per_week = 4 * 3

    # Calculate Zainab's earnings per week
    weekly_earnings = hours_per_week * RATE

    # Calculate Zainab's total earnings over the 4 weeks
    total_earnings = weekly_earnings * 4

    # Display Zainab's total earnings
    result = total_earnings
    return result

print(solution())