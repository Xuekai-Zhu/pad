def solution():
    hour_rate = 10
    hours_first_month = 35
    hours_second_month = hours_first_month + 5
    total_hours = hours_first_month + hours_second_month
    total_earnings = total_hours * hour_rate
    savings = total_earnings - (total_earnings * 4/5)
    result = savings
    return result

print(solution())