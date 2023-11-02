def solution():
    """James trains for the Olympics. He trains twice a day for 4 hours each time for all but 2 days per week. How many hours does he train a year?"""
    # Define the number of days in a week and in a year
    WEEK_DAYS = 7
    YEAR_DAYS = 365

    # Define the number of training hours per session and per week
    SESSION_HOURS = 4
    WEEKLY_HOURS = 4 * 2 * (WEEK_DAYS - 2)

    # Calculate the total hours trained in a year
    yearly_hours = WEEKLY_HOURS * (YEAR_DAYS // WEEK_DAYS)

    # Display the total training hours per year
    result = yearly_hours
    return result

print(solution())