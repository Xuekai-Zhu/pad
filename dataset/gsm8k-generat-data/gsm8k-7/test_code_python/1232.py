def solution():
    num_hours_per_day = 8
    hourly_rate = 7.5
    num_days_per_month = 20
    num_months = 2

    # Calculate the total number of hours worked per month
    total_hours_per_month = num_hours_per_day * num_days_per_month

    # Calculate the total earnings per month
    total_earnings_per_month = total_hours_per_month * hourly_rate

    # Calculate the total earnings for two months of work
    total_earnings_for_two_months = total_earnings_per_month * num_months
    result = total_earnings_for_two_months
    return result

print(solution())