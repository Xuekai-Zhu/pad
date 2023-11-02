def solution():
    """On a tough week, Haji's mother sells goods worth $800, which is half the amount she sells on a good week. What's the total amount of money she makes if she has 5 good weeks and 3 tough weeks?"""
    # Define the amount of money earned on a tough week and a good week
    tough_week_earnings = 800
    good_week_earnings = tough_week_earnings * 2

    # Calculate the total earnings for 5 good weeks and 3 tough weeks
    total_earnings = (5 * good_week_earnings) + (3 * tough_week_earnings)

    # Return the result
    result = total_earnings
    return result

print(solution())