def solution():
    """During the Christmas holidays, all shops are closed for 3 days. During each day during this time, a shop called "Surprise" could have earned 5 thousand dollars. How much potential revenue did the "Surprise" shop lose during 6 years of activity?"""
    # Define the number of years of activity and the potential revenue per day
    YEARS_OF_ACTIVITY = 6
    REVENUE_PER_DAY = 5000

    # Calculate the number of days that the shop was closed during the Christmas holidays
    days_closed = 3 * 6

    # Calculate the potential revenue lost during the Christmas holidays for 6 years of activity
    revenue_lost = days_closed * REVENUE_PER_DAY

    # return the result
    result = revenue_lost
    return result

print(solution())