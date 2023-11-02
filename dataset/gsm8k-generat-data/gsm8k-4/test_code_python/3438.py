def solution():
    """Penn operates an ice cream stall for a week. On the first day, she made $10. Every day after that, she made $4 more than the previous day. How much money did Penn make after 5 days?"""
    # Define the initial earnings and the daily increase
    initial_earnings = 10
    daily_increase = 4

    # Initialize the total earnings counter
    total_earnings = initial_earnings

    # Calculate the earnings after 5 days
    for i in range(1, 5):
        daily_earnings = initial_earnings + (i * daily_increase)
        total_earnings += daily_earnings

    # Add the earnings of the fifth day
    total_earnings += initial_earnings + (5 * daily_increase)

    # return the result
    result = total_earnings
    return result

print(solution())