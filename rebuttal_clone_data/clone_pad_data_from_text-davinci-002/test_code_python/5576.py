def solution ():
    hours_per_week = 5 * 5 + 2 * 3
    hourly_rate = 3
    weekend_rate = 2 * hourly_rate
    total_earnings = hours_per_week * hourly_rate + 2 * weekend_rate
    result = total_earnings
    return result

print(solution())