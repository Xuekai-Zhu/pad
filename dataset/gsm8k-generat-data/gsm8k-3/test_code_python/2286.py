def solution():
    """Marta works on her grandparent's farm to raise money for a new phone. So far, she has collected $240. For every hour she works, she receives $10. Her grandmother often gives her tips, and she has collected $50 in tips in total. How many hours has Marta worked on the farm so far?"""
    # Define Marta's earnings per hour and tips received
    HOURLY_EARNINGS = 10
    TIPS_RECEIVED = 50

    # Define Marta's total earnings
    total_earnings = 240 + TIPS_RECEIVED

    # Calculate the number of hours Marta has worked
    hours_worked = total_earnings / HOURLY_EARNINGS

    # Display the number of hours Marta has worked
    result = hours_worked
    return result

print(solution())