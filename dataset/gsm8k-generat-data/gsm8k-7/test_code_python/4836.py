def solution():
    visits_per_hour = 50
    earnings_per_visit = 0.10
    hours_per_day = 24
    days_per_month = 30

    # Calculate the total number of visits in a month
    total_visits = visits_per_hour * hours_per_day * days_per_month

    # Calculate the total earnings from all visits in a month
    total_earnings = total_visits * earnings_per_visit
    result = total_earnings
    return result

print(solution())