def solution():
    hourly_rate = 5
    hours_week1 = 20
    hours_week2 = 30

    earnings_week1 = hours_week1 * hourly_rate
    earnings_week2 = hours_week2 * hourly_rate

    total_earnings = earnings_week1 + earnings_week2
    result = total_earnings
    return result

print(solution())