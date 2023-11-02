def solution():
    visits_per_hour = 50  # Jon gets 50 visits to his website every hour
    hours_per_day = 24  # Jon's website operates 24 hours per day
    days_per_month = 30  # There are 30 days in a month

    # Calculate the total number of visits Jon gets in a month
    total_visits = visits_per_hour * hours_per_day * days_per_month

    # Calculate the total amount of money Jon makes in a month
    total_money = total_visits * 0.10  # Jon gets paid $0.10 per visit

    result = total_money
    return result

print(solution())