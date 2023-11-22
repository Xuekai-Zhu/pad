def solution():
    
    # Define the number of weeks and days per week
    WEEKS_PER_MONTH = 4
    DAYS_PER_WEEK = 6

    # Define the number of days in a year
    DAYS_PER_YEAR = 365 * WEEKS_PER_MONTH * DAYS_PER_WEEK

    # Define the pay rate per day
    PAY_RATE_PER_DAY = 50

    # Calculate the total pay for a year
    total_pay = DAYS_PER_YEAR * PAY_RATE_PER_DAY

    # Display the total pay for a year
    result = total_pay
    return result

print(solution())