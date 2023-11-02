def solution():
    workdays_in_two_weeks = 10  # Susan works 5 days a week for 2 weeks, minus the 6 days of paid vacation
    unpaid_days = workdays_in_two_weeks - 6  # Susan has 6 days of paid vacation, the rest are unpaid
    daily_pay = 15 * 8  # Susan gets paid $15 per hour and works 8 hours a day

    # Calculate the total pay Susan will miss on her unpaid vacation days
    unpaid_pay = unpaid_days * daily_pay
    result = unpaid_pay
    return result

print(solution())