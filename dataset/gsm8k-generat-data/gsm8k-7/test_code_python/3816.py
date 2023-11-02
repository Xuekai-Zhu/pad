def solution():
    hourly_rate = 5
    hours_week1 = 20
    hours_week2 = 30

    # Calculate the total earnings for the first week
    earnings_week1 = hourly_rate * hours_week1

    # Calculate the total earnings for the second week
    earnings_week2 = hourly_rate * hours_week2

    # Calculate the total earnings for two weeks
    total_earnings = earnings_week1 + earnings_week2
    result = total_earnings
    return result

print(solution())