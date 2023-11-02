def solution():
    hourly_rate = 10  # Lloyd earns $10 an hour on Math tutoring
    hours_week1 = 5  # Lloyd tutored 5 hours for the first week
    hours_week2 = 8  # Lloyd tutored 8 hours for the second week

    # Calculate Lloyd's earnings for the first two weeks
    earnings_week1 = hourly_rate * hours_week1
    earnings_week2 = hourly_rate * hours_week2
    total_earnings = earnings_week1 + earnings_week2
    result = total_earnings
    return result

print(solution())