def solution():
    """Goldie makes $5 an hour for pet-sitting. Last week, she worked for 20 hours while this week, she worked for 30 hours. How much did Goldie earn in two weeks for pet-sitting?"""
    # Define the hourly rate and the number of hours worked each week
    HOURLY_RATE = 5
    WEEK_1_HOURS = 20
    WEEK_2_HOURS = 30

    # Calculate the earnings for each week
    week_1_earnings = HOURLY_RATE * WEEK_1_HOURS
    week_2_earnings = HOURLY_RATE * WEEK_2_HOURS

    # Calculate the total earnings for two weeks
    total_earnings = week_1_earnings + week_2_earnings

    # return the result
    result = total_earnings
    return result

print(solution())