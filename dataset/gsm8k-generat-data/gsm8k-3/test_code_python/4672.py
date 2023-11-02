def solution():
    """Amanda charges $20.00 per hour to help clean out and organize a person's home. She has 5 1.5 hours appointments 
    on Monday, a 3-hours appointment on Tuesday and 2 2-hours appointments on Thursday. On Saturday, she will spend 6 
    hours at one client's house. How much money will she make this week?"""
    
    # Define the hourly rate
    HOURLY_RATE = 20

    # Calculate the total earnings for each day
    monday_earnings = 5 * 1.5 * HOURLY_RATE
    tuesday_earnings = 3 * HOURLY_RATE
    thursday_earnings = 2 * 2 * HOURLY_RATE
    saturday_earnings = 6 * HOURLY_RATE

    # Calculate the total earnings for the week
    total_earnings = monday_earnings + tuesday_earnings + thursday_earnings + saturday_earnings

    # Display the total earnings for the week
    result = total_earnings
    return result

print(solution())