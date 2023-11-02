def solution():
    """Amanda charges $20.00 per hour to help clean out and organize a person's home. She has 5 1.5 hours appointments on Monday, a 3-hours appointment on Tuesday and 2 2-hours appointments on Thursday. On Saturday, she will spend 6 hours at one client's house. How much money will she make this week?"""
    # Define the hourly rate and the number of hours worked each day
    HOURLY_RATE = 20
    monday_hours = 5 * 1.5
    tuesday_hours = 3
    thursday_hours = 2 * 2
    saturday_hours = 6

    # Calculate the total number of hours worked
    total_hours = monday_hours + tuesday_hours + thursday_hours + saturday_hours

    # Calculate the total earnings for the week
    total_earnings = total_hours * HOURLY_RATE

    # Display the total earnings
    result = total_earnings
    return result

print(solution())