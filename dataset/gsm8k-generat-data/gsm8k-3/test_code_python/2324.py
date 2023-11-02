def solution():
    """Isabella earns $5 an hour babysitting. She babysits 5 hours every day, 6 afternoons a week. After babysitting for 7 weeks, how much money will Isabella have earned?"""
    # Define the rate and hours worked per day
    RATE = 5
    HOURS_PER_DAY = 5

    # Calculate the total hours worked per week
    hours_per_week = HOURS_PER_DAY * 6

    # Calculate the total hours worked over 7 weeks
    total_hours = hours_per_week * 7

    # Calculate Isabella's earnings
    earnings = total_hours * RATE

    # Display Isabella's earnings
    result = earnings
    return result

print(solution())