def solution():
    periods_per_day = 5  # The teacher teaches 5 periods a day
    days_per_month = 24  # The teacher works 24 days a month
    pay_per_period = 5  # The teacher is paid $5 per period
    months_worked = 6  # The teacher has been working for 6 months

    # Calculate the total number of periods taught
    total_periods = periods_per_day * days_per_month * months_worked

    # Calculate the total amount earned
    total_earnings = total_periods * pay_per_period

    result = total_earnings
    return result

print(solution())