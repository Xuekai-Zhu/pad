def solution():
    """Olivia earns $9 per hour. She worked 4 hours on Monday, 3 hours on Wednesday and 6 hours on Friday. How much money did Olivia make this week?"""
    # Define Olivia's hourly rate and the hours worked each day
    HOURLY_RATE = 9
    HOURS_WORKED = [4, 3, 6]

    # Calculate the total hours worked
    total_hours = sum(HOURS_WORKED)

    # Calculate Olivia's total earnings for the week
    earnings = total_hours * HOURLY_RATE

    # return the result
    result = earnings
    return result

print(solution())