def solution():
    first_day_earnings = 10
    daily_increase = 4
    num_days = 5

    total_earnings = first_day_earnings

    for i in range(1, num_days):
        earnings = first_day_earnings + (i * daily_increase)
        total_earnings += earnings

    result = total_earnings
    return result

print(solution())