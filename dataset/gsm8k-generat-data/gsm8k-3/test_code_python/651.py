def solution():
    """Olivia earns $9 per hour. She worked 4 hours on Monday, 3 hours on Wednesday and 6 hours on Friday. How much money did Olivia make this week?"""
    # Define Olivia's hourly rate
    HOURLY_RATE = 9

    # Calculate Olivia's earnings for each day
    monday_earnings = 4 * HOURLY_RATE
    wednesday_earnings = 3 * HOURLY_RATE
    friday_earnings = 6 * HOURLY_RATE

    # Calculate Olivia's total earnings for the week
    total_earnings = monday_earnings + wednesday_earnings + friday_earnings

    # Display Olivia's total earnings
    result = total_earnings
    return result

print(solution())