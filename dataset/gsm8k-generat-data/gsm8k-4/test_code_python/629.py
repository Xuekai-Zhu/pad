def solution():
    """A teacher teaches 5 periods a day and works 24 days a month. He is paid $5 per period. if he has been working for 6 months now how much has he earned in total?"""
    # Define the number of periods taught per day and the number of days worked in a month
    PERIODS_PER_DAY = 5
    DAYS_WORKED_PER_MONTH = 24

    # Define the teacher's pay per period
    PAY_PER_PERIOD = 5

    # Define the number of months worked
    MONTHS_WORKED = 6

    # Calculate the total number of periods taught
    total_periods = PERIODS_PER_DAY * DAYS_WORKED_PER_MONTH * MONTHS_WORKED

    # Calculate the total earnings
    total_earnings = total_periods * PAY_PER_PERIOD

    result = total_earnings
    return result

print(solution())